from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.page_contact import PageContact
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    keyword: Union[Unset, str] = UNSET,
    contact_handle_token: Union[Unset, List[str]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["keyword"] = keyword

    json_contact_handle_token: Union[Unset, List[str]] = UNSET
    if not isinstance(contact_handle_token, Unset):
        json_contact_handle_token = contact_handle_token

    params["contact_handle_token"] = json_contact_handle_token

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/v1/contacts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[PageContact]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PageContact.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[PageContact]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    contact_handle_token: Union[Unset, List[str]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageContact]:
    """List contacts

    Args:
        keyword (Union[Unset, str]):
        contact_handle_token (Union[Unset, List[str]]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageContact]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        contact_handle_token=contact_handle_token,
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
    keyword: Union[Unset, str] = UNSET,
    contact_handle_token: Union[Unset, List[str]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageContact]:
    """List contacts

    Args:
        keyword (Union[Unset, str]):
        contact_handle_token (Union[Unset, List[str]]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageContact
    """

    return sync_detailed(
        client=client,
        keyword=keyword,
        contact_handle_token=contact_handle_token,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    contact_handle_token: Union[Unset, List[str]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[PageContact]:
    """List contacts

    Args:
        keyword (Union[Unset, str]):
        contact_handle_token (Union[Unset, List[str]]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PageContact]
    """

    kwargs = _get_kwargs(
        keyword=keyword,
        contact_handle_token=contact_handle_token,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    keyword: Union[Unset, str] = UNSET,
    contact_handle_token: Union[Unset, List[str]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[PageContact]:
    """List contacts

    Args:
        keyword (Union[Unset, str]):
        contact_handle_token (Union[Unset, List[str]]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PageContact
    """

    return (
        await asyncio_detailed(
            client=client,
            keyword=keyword,
            contact_handle_token=contact_handle_token,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
