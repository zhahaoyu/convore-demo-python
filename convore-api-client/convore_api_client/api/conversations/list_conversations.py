import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.conversation_status import ConversationStatus
from ...models.page_conversation import PageConversation
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel_id: Union[Unset, str] = UNSET,
    status: Union[Unset, ConversationStatus] = UNSET,
    statuses: Union[Unset, List[ConversationStatus]] = UNSET,
    label_ids: Union[Unset, List[str]] = UNSET,
    has_no_label: Union[Unset, bool] = UNSET,
    contact_handle_token: Union[Unset, str] = UNSET,
    has_drafts: Union[Unset, bool] = UNSET,
    has_messages: Union[Unset, bool] = UNSET,
    has_outbound_messages: Union[Unset, bool] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_before: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_after: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["channel_id"] = channel_id

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_statuses: Union[Unset, List[str]] = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = []
        for statuses_item_data in statuses:
            statuses_item = statuses_item_data.value
            json_statuses.append(statuses_item)

    params["statuses"] = json_statuses

    json_label_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(label_ids, Unset):
        json_label_ids = label_ids

    params["label_ids"] = json_label_ids

    params["has_no_label"] = has_no_label

    params["contact_handle_token"] = contact_handle_token

    params["has_drafts"] = has_drafts

    params["has_messages"] = has_messages

    params["has_outbound_messages"] = has_outbound_messages

    json_created_at_before: Union[Unset, str] = UNSET
    if not isinstance(created_at_before, Unset):
        json_created_at_before = created_at_before.isoformat()
    params["created_at_before"] = json_created_at_before

    json_created_at_after: Union[Unset, str] = UNSET
    if not isinstance(created_at_after, Unset):
        json_created_at_after = created_at_after.isoformat()
    params["created_at_after"] = json_created_at_after

    json_last_message_date_before: Union[Unset, str] = UNSET
    if not isinstance(last_message_date_before, Unset):
        json_last_message_date_before = last_message_date_before.isoformat()
    params["last_message_date_before"] = json_last_message_date_before

    json_last_message_date_after: Union[Unset, str] = UNSET
    if not isinstance(last_message_date_after, Unset):
        json_last_message_date_after = last_message_date_after.isoformat()
    params["last_message_date_after"] = json_last_message_date_after

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/conversations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PageConversation]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PageConversation.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PageConversation]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    channel_id: Union[Unset, str] = UNSET,
    status: Union[Unset, ConversationStatus] = UNSET,
    statuses: Union[Unset, List[ConversationStatus]] = UNSET,
    label_ids: Union[Unset, List[str]] = UNSET,
    has_no_label: Union[Unset, bool] = UNSET,
    contact_handle_token: Union[Unset, str] = UNSET,
    has_drafts: Union[Unset, bool] = UNSET,
    has_messages: Union[Unset, bool] = UNSET,
    has_outbound_messages: Union[Unset, bool] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_before: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_after: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageConversation]:
    """List conversations

    Args:
        channel_id (Union[Unset, str]):
        status (Union[Unset, ConversationStatus]): Status of the conversation
        statuses (Union[Unset, List[ConversationStatus]]):
        label_ids (Union[Unset, List[str]]):
        has_no_label (Union[Unset, bool]):
        contact_handle_token (Union[Unset, str]):
        has_drafts (Union[Unset, bool]):
        has_messages (Union[Unset, bool]):
        has_outbound_messages (Union[Unset, bool]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):
        last_message_date_before (Union[Unset, datetime.datetime]):
        last_message_date_after (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageConversation]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        status=status,
        statuses=statuses,
        label_ids=label_ids,
        has_no_label=has_no_label,
        contact_handle_token=contact_handle_token,
        has_drafts=has_drafts,
        has_messages=has_messages,
        has_outbound_messages=has_outbound_messages,
        created_at_before=created_at_before,
        created_at_after=created_at_after,
        last_message_date_before=last_message_date_before,
        last_message_date_after=last_message_date_after,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    channel_id: Union[Unset, str] = UNSET,
    status: Union[Unset, ConversationStatus] = UNSET,
    statuses: Union[Unset, List[ConversationStatus]] = UNSET,
    label_ids: Union[Unset, List[str]] = UNSET,
    has_no_label: Union[Unset, bool] = UNSET,
    contact_handle_token: Union[Unset, str] = UNSET,
    has_drafts: Union[Unset, bool] = UNSET,
    has_messages: Union[Unset, bool] = UNSET,
    has_outbound_messages: Union[Unset, bool] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_before: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_after: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageConversation]:
    """List conversations

    Args:
        channel_id (Union[Unset, str]):
        status (Union[Unset, ConversationStatus]): Status of the conversation
        statuses (Union[Unset, List[ConversationStatus]]):
        label_ids (Union[Unset, List[str]]):
        has_no_label (Union[Unset, bool]):
        contact_handle_token (Union[Unset, str]):
        has_drafts (Union[Unset, bool]):
        has_messages (Union[Unset, bool]):
        has_outbound_messages (Union[Unset, bool]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):
        last_message_date_before (Union[Unset, datetime.datetime]):
        last_message_date_after (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageConversation
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        status=status,
        statuses=statuses,
        label_ids=label_ids,
        has_no_label=has_no_label,
        contact_handle_token=contact_handle_token,
        has_drafts=has_drafts,
        has_messages=has_messages,
        has_outbound_messages=has_outbound_messages,
        created_at_before=created_at_before,
        created_at_after=created_at_after,
        last_message_date_before=last_message_date_before,
        last_message_date_after=last_message_date_after,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    channel_id: Union[Unset, str] = UNSET,
    status: Union[Unset, ConversationStatus] = UNSET,
    statuses: Union[Unset, List[ConversationStatus]] = UNSET,
    label_ids: Union[Unset, List[str]] = UNSET,
    has_no_label: Union[Unset, bool] = UNSET,
    contact_handle_token: Union[Unset, str] = UNSET,
    has_drafts: Union[Unset, bool] = UNSET,
    has_messages: Union[Unset, bool] = UNSET,
    has_outbound_messages: Union[Unset, bool] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_before: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_after: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageConversation]:
    """List conversations

    Args:
        channel_id (Union[Unset, str]):
        status (Union[Unset, ConversationStatus]): Status of the conversation
        statuses (Union[Unset, List[ConversationStatus]]):
        label_ids (Union[Unset, List[str]]):
        has_no_label (Union[Unset, bool]):
        contact_handle_token (Union[Unset, str]):
        has_drafts (Union[Unset, bool]):
        has_messages (Union[Unset, bool]):
        has_outbound_messages (Union[Unset, bool]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):
        last_message_date_before (Union[Unset, datetime.datetime]):
        last_message_date_after (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageConversation]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        status=status,
        statuses=statuses,
        label_ids=label_ids,
        has_no_label=has_no_label,
        contact_handle_token=contact_handle_token,
        has_drafts=has_drafts,
        has_messages=has_messages,
        has_outbound_messages=has_outbound_messages,
        created_at_before=created_at_before,
        created_at_after=created_at_after,
        last_message_date_before=last_message_date_before,
        last_message_date_after=last_message_date_after,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    channel_id: Union[Unset, str] = UNSET,
    status: Union[Unset, ConversationStatus] = UNSET,
    statuses: Union[Unset, List[ConversationStatus]] = UNSET,
    label_ids: Union[Unset, List[str]] = UNSET,
    has_no_label: Union[Unset, bool] = UNSET,
    contact_handle_token: Union[Unset, str] = UNSET,
    has_drafts: Union[Unset, bool] = UNSET,
    has_messages: Union[Unset, bool] = UNSET,
    has_outbound_messages: Union[Unset, bool] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_before: Union[Unset, datetime.datetime] = UNSET,
    last_message_date_after: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageConversation]:
    """List conversations

    Args:
        channel_id (Union[Unset, str]):
        status (Union[Unset, ConversationStatus]): Status of the conversation
        statuses (Union[Unset, List[ConversationStatus]]):
        label_ids (Union[Unset, List[str]]):
        has_no_label (Union[Unset, bool]):
        contact_handle_token (Union[Unset, str]):
        has_drafts (Union[Unset, bool]):
        has_messages (Union[Unset, bool]):
        has_outbound_messages (Union[Unset, bool]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):
        last_message_date_before (Union[Unset, datetime.datetime]):
        last_message_date_after (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageConversation
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            status=status,
            statuses=statuses,
            label_ids=label_ids,
            has_no_label=has_no_label,
            contact_handle_token=contact_handle_token,
            has_drafts=has_drafts,
            has_messages=has_messages,
            has_outbound_messages=has_outbound_messages,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
            last_message_date_before=last_message_date_before,
            last_message_date_after=last_message_date_after,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
