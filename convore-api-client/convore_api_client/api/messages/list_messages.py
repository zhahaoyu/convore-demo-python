from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_format import MessageFormat
from ...models.page_message import PageMessage
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    conversation_id: Union[Unset, str] = UNSET,
    format_: Union[Unset, MessageFormat] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["conversation_id"] = conversation_id

    json_format_: Union[Unset, str] = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/messages",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PageMessage]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PageMessage.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PageMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conversation_id: Union[Unset, str] = UNSET,
    format_: Union[Unset, MessageFormat] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageMessage]:
    """List messages

    Args:
        conversation_id (Union[Unset, str]):
        format_ (Union[Unset, MessageFormat]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageMessage]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        format_=format_,
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
    conversation_id: Union[Unset, str] = UNSET,
    format_: Union[Unset, MessageFormat] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageMessage]:
    """List messages

    Args:
        conversation_id (Union[Unset, str]):
        format_ (Union[Unset, MessageFormat]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageMessage
    """

    return sync_detailed(
        client=client,
        conversation_id=conversation_id,
        format_=format_,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    conversation_id: Union[Unset, str] = UNSET,
    format_: Union[Unset, MessageFormat] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageMessage]:
    """List messages

    Args:
        conversation_id (Union[Unset, str]):
        format_ (Union[Unset, MessageFormat]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageMessage]
    """

    kwargs = _get_kwargs(
        conversation_id=conversation_id,
        format_=format_,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    conversation_id: Union[Unset, str] = UNSET,
    format_: Union[Unset, MessageFormat] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageMessage]:
    """List messages

    Args:
        conversation_id (Union[Unset, str]):
        format_ (Union[Unset, MessageFormat]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageMessage
    """

    return (
        await asyncio_detailed(
            client=client,
            conversation_id=conversation_id,
            format_=format_,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
