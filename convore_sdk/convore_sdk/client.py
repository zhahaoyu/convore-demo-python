from typing import Optional

import convore_api_client
from convore_sdk.subscriptions import (SubscriptionsApi,
                                       SubscriptionApiConfiguration)


class Convore:

  def __init__(self, api_key: str, base_url: str = "https://api.convore.dev",
      subscription: Optional[
        SubscriptionApiConfiguration] = SubscriptionApiConfiguration()):
    configuration = convore_api_client.Configuration(
        host=base_url,
        access_token=api_key,
    )
    self.api_client = convore_api_client.ApiClient(configuration)
    self.attachments = convore_api_client.AttachmentsApi(self.api_client)
    self.authorization_flows = convore_api_client.AuthorizationFlowsApi(
        self.api_client)
    self.connectors = convore_api_client.ConnectorsApi(self.api_client)
    self.contacts = convore_api_client.ContactsApi(self.api_client)
    self.drafts = convore_api_client.DraftsApi(self.api_client)
    self.events = convore_api_client.EventsApi(self.api_client)
    self.channels = convore_api_client.ChannelsApi(self.api_client)
    self.labels = convore_api_client.LabelsApi(self.api_client)
    self.conversations = convore_api_client.ConversationsApi(self.api_client)
    self.messages = convore_api_client.MessagesApi(self.api_client)
    self.subscriptions = SubscriptionsApi(configuration,
                                         subscription)
