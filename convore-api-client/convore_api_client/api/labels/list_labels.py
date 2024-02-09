from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.label_type import LabelType
from ...models.page_label import PageLabel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel_id: Union[Unset, List[str]] = UNSET,
    channel_ids: Union[Unset, List[str]] = UNSET,
    type: Union[Unset, LabelType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_channel_id: Union[Unset, List[str]] = UNSET
    if not isinstance(channel_id, Unset):
        json_channel_id = channel_id

    params["channel_id"] = json_channel_id

    json_channel_ids: Union[Unset, List[str]] = UNSET
    if not isinstance(channel_ids, Unset):
        json_channel_ids = channel_ids

    params["channel_ids"] = json_channel_ids

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/labels",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PageLabel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PageLabel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PageLabel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    channel_id: Union[Unset, List[str]] = UNSET,
    channel_ids: Union[Unset, List[str]] = UNSET,
    type: Union[Unset, LabelType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageLabel]:
    """List labels

    Args:
        channel_id (Union[Unset, List[str]]):
        channel_ids (Union[Unset, List[str]]):
        type (Union[Unset, LabelType]): The type of the label, which determines its scope and
            usage. 'SHARED' labels are accessible across multiple channels, while 'CHANNEL_PRIVATE'
            labels are restricted to a specific channel. Note: When a 'SHARED' label is created and
            later applied to a conversation, the API automatically applies the corresponding
            'CHANNEL_PRIVATE' label to the conversation in the specific channel, and vice versa.
            Example: SHARED.
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageLabel]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        channel_ids=channel_ids,
        type=type,
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
    channel_id: Union[Unset, List[str]] = UNSET,
    channel_ids: Union[Unset, List[str]] = UNSET,
    type: Union[Unset, LabelType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageLabel]:
    """List labels

    Args:
        channel_id (Union[Unset, List[str]]):
        channel_ids (Union[Unset, List[str]]):
        type (Union[Unset, LabelType]): The type of the label, which determines its scope and
            usage. 'SHARED' labels are accessible across multiple channels, while 'CHANNEL_PRIVATE'
            labels are restricted to a specific channel. Note: When a 'SHARED' label is created and
            later applied to a conversation, the API automatically applies the corresponding
            'CHANNEL_PRIVATE' label to the conversation in the specific channel, and vice versa.
            Example: SHARED.
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageLabel
    """

    return sync_detailed(
        client=client,
        channel_id=channel_id,
        channel_ids=channel_ids,
        type=type,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    channel_id: Union[Unset, List[str]] = UNSET,
    channel_ids: Union[Unset, List[str]] = UNSET,
    type: Union[Unset, LabelType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageLabel]:
    """List labels

    Args:
        channel_id (Union[Unset, List[str]]):
        channel_ids (Union[Unset, List[str]]):
        type (Union[Unset, LabelType]): The type of the label, which determines its scope and
            usage. 'SHARED' labels are accessible across multiple channels, while 'CHANNEL_PRIVATE'
            labels are restricted to a specific channel. Note: When a 'SHARED' label is created and
            later applied to a conversation, the API automatically applies the corresponding
            'CHANNEL_PRIVATE' label to the conversation in the specific channel, and vice versa.
            Example: SHARED.
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageLabel]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        channel_ids=channel_ids,
        type=type,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    channel_id: Union[Unset, List[str]] = UNSET,
    channel_ids: Union[Unset, List[str]] = UNSET,
    type: Union[Unset, LabelType] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageLabel]:
    """List labels

    Args:
        channel_id (Union[Unset, List[str]]):
        channel_ids (Union[Unset, List[str]]):
        type (Union[Unset, LabelType]): The type of the label, which determines its scope and
            usage. 'SHARED' labels are accessible across multiple channels, while 'CHANNEL_PRIVATE'
            labels are restricted to a specific channel. Note: When a 'SHARED' label is created and
            later applied to a conversation, the API automatically applies the corresponding
            'CHANNEL_PRIVATE' label to the conversation in the specific channel, and vice versa.
            Example: SHARED.
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageLabel
    """

    return (
        await asyncio_detailed(
            client=client,
            channel_id=channel_id,
            channel_ids=channel_ids,
            type=type,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
