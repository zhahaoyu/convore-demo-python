import json
import os
import time
from datetime import datetime, timedelta, timezone
from threading import Thread, Lock
from typing import Protocol, Dict, Set
from uuid import uuid4

import convore_api_client
from convore_api_client import Configuration, EventsApi, ApiException
from convore_api_client.models import Event, EventType
from pydantic import BaseModel


class EventHandler(Protocol):
    def __call__(self, event: Event) -> None:
        pass


class Subscription:
    def __init__(self, event_types: Set[EventType], handler: EventHandler):
        self.id = str(uuid4())
        self.event_types = event_types
        self.handler = handler


class SubscriptionApiConfiguration(BaseModel):
    event_history_file: str = "./events.json"
    polling_interval: int = 1
    created_after: datetime = datetime.now(timezone.utc)
    look_back_window: int = 1000


class SubscriptionsApi:
    def __init__(self,
                 configuration: Configuration,
                 sdk_configuration: SubscriptionApiConfiguration):
        self.subscriptions: Dict[str, Subscription] = {}
        self.is_running = False
        self.polling_interval = sdk_configuration.polling_interval
        self.event_history_file = sdk_configuration.event_history_file
        self.event_history = self._read_event_history()
        self.created_after = sdk_configuration.created_after
        self.look_back_window = sdk_configuration.look_back_window
        self.lock = Lock()
        self.api_client = convore_api_client.ApiClient(configuration)
        self.events_api = EventsApi(self.api_client)

    def on(self, event_types: Set[EventType], handler: EventHandler) -> None:
        subscription = Subscription(event_types, handler)
        self.subscriptions[subscription.id] = subscription

    def remove(self, subscription_id: str) -> None:
        if subscription_id in self.subscriptions:
            del self.subscriptions[subscription_id]

    def _read_event_history(self) -> Dict[str, Event]:
        if os.path.exists(self.event_history_file):
            with open(self.event_history_file, 'r') as file:
                event_history_dict = json.load(file)
            # Convert each dictionary back into an Event object
            return {event_id: Event.from_json(event_json) for event_id, event_json in
                    event_history_dict.items()}
        return {}

    def _write_event_history(self) -> None:
        # Convert each Event object to its dictionary representation
        event_history_dict = {event_id: event.model_dump_json() for event_id, event in
                              self.event_history.items()}
        with open(self.event_history_file, 'w') as file:
            json.dump(event_history_dict, file)

    def _is_event_seen(self, event_id: str) -> bool:
        return event_id in self.event_history

    def _ack(self, event: Event) -> None:
        self.event_history[event.id] = event
        self._write_event_history()

    def _poll(self) -> None:
        with self.lock:
            events = self._list_new_events(self.created_after)

            for event in events:
                if not self._is_event_seen(event.id):
                    for subscription in self.subscriptions.values():
                        if event.type in subscription.event_types:
                            try:
                                subscription.handler(event)
                            except Exception as e:
                                print(f"Error handling event {event.id}: {e}")
                                raise e
                    self._ack(event)

            if events:
                newest_event = max(events, key=lambda e: e.created_at)
                self.created_after = max(self.created_after,
                                         newest_event.created_at - timedelta(
                                             milliseconds=self.look_back_window))

    def listen(self) -> None:
        Thread(target=self._start_polling).start()

    def _start_polling(self) -> None:
        while True:
            self._poll()
            time.sleep(self.polling_interval)

    def _list_new_events(self, created_at_after: datetime) -> list[Event]:
        has_more = True
        cursor = None
        events = []
        while has_more:
            try:
                # Create an API key
                page = self.events_api.list_events(
                    created_at_after=created_at_after,
                    cursor=cursor,
                    limit=10)
                cursor = page.next_cursor
                has_more = cursor is not None

                events.extend(page.data)
            except ApiException as e:
                print("Exception when calling EventsApi->list_events: %s\n" % e)
            except Exception as e:
                print("Exception when calling EventsApi->list_events: %s\n" % e)
        return events
