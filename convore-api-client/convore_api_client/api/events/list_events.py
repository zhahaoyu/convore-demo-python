import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_type import EventType
from ...models.object_type import ObjectType
from ...models.page_event import PageEvent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    types: Union[Unset, List[EventType]] = UNSET,
    type: Union[Unset, EventType] = UNSET,
    object_id: Union[Unset, str] = UNSET,
    object_type: Union[Unset, ObjectType] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["cursor"] = cursor

    params["limit"] = limit

    json_types: Union[Unset, List[str]] = UNSET
    if not isinstance(types, Unset):
        json_types = []
        for types_item_data in types:
            types_item = types_item_data.value
            json_types.append(types_item)

    params["types"] = json_types

    json_type: Union[Unset, str] = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params["object_id"] = object_id

    json_object_type: Union[Unset, str] = UNSET
    if not isinstance(object_type, Unset):
        json_object_type = object_type.value

    params["object_type"] = json_object_type

    json_created_at_before: Union[Unset, str] = UNSET
    if not isinstance(created_at_before, Unset):
        json_created_at_before = created_at_before.isoformat()
    params["created_at_before"] = json_created_at_before

    json_created_at_after: Union[Unset, str] = UNSET
    if not isinstance(created_at_after, Unset):
        json_created_at_after = created_at_after.isoformat()
    params["created_at_after"] = json_created_at_after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/events",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PageEvent]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PageEvent.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PageEvent]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    types: Union[Unset, List[EventType]] = UNSET,
    type: Union[Unset, EventType] = UNSET,
    object_id: Union[Unset, str] = UNSET,
    object_type: Union[Unset, ObjectType] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
) -> Response[PageEvent]:
    """List events

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        types (Union[Unset, List[EventType]]):
        type (Union[Unset, EventType]):
        object_id (Union[Unset, str]):
        object_type (Union[Unset, ObjectType]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageEvent]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        types=types,
        type=type,
        object_id=object_id,
        object_type=object_type,
        created_at_before=created_at_before,
        created_at_after=created_at_after,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    types: Union[Unset, List[EventType]] = UNSET,
    type: Union[Unset, EventType] = UNSET,
    object_id: Union[Unset, str] = UNSET,
    object_type: Union[Unset, ObjectType] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[PageEvent]:
    """List events

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        types (Union[Unset, List[EventType]]):
        type (Union[Unset, EventType]):
        object_id (Union[Unset, str]):
        object_type (Union[Unset, ObjectType]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageEvent
    """

    return sync_detailed(
        client=client,
        cursor=cursor,
        limit=limit,
        types=types,
        type=type,
        object_id=object_id,
        object_type=object_type,
        created_at_before=created_at_before,
        created_at_after=created_at_after,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    types: Union[Unset, List[EventType]] = UNSET,
    type: Union[Unset, EventType] = UNSET,
    object_id: Union[Unset, str] = UNSET,
    object_type: Union[Unset, ObjectType] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
) -> Response[PageEvent]:
    """List events

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        types (Union[Unset, List[EventType]]):
        type (Union[Unset, EventType]):
        object_id (Union[Unset, str]):
        object_type (Union[Unset, ObjectType]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageEvent]
    """

    kwargs = _get_kwargs(
        cursor=cursor,
        limit=limit,
        types=types,
        type=type,
        object_id=object_id,
        object_type=object_type,
        created_at_before=created_at_before,
        created_at_after=created_at_after,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
    types: Union[Unset, List[EventType]] = UNSET,
    type: Union[Unset, EventType] = UNSET,
    object_id: Union[Unset, str] = UNSET,
    object_type: Union[Unset, ObjectType] = UNSET,
    created_at_before: Union[Unset, datetime.datetime] = UNSET,
    created_at_after: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[PageEvent]:
    """List events

    Args:
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.
        types (Union[Unset, List[EventType]]):
        type (Union[Unset, EventType]):
        object_id (Union[Unset, str]):
        object_type (Union[Unset, ObjectType]):
        created_at_before (Union[Unset, datetime.datetime]):
        created_at_after (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageEvent
    """

    return (
        await asyncio_detailed(
            client=client,
            cursor=cursor,
            limit=limit,
            types=types,
            type=type,
            object_id=object_id,
            object_type=object_type,
            created_at_before=created_at_before,
            created_at_after=created_at_after,
        )
    ).parsed
