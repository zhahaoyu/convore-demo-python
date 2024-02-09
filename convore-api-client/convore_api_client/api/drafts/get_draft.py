from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.draft import Draft
from ...types import Response


def _get_kwargs(
    draft_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/v1/drafts/{draft_id}",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Draft]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Draft.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Draft]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    draft_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Draft]:
    """Retrieve a draft

    Args:
        draft_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Draft]
    """

    kwargs = _get_kwargs(
        draft_id=draft_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    draft_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Draft]:
    """Retrieve a draft

    Args:
        draft_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Draft
    """

    return sync_detailed(
        draft_id=draft_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    draft_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Draft]:
    """Retrieve a draft

    Args:
        draft_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Draft]
    """

    kwargs = _get_kwargs(
        draft_id=draft_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    draft_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Draft]:
    """Retrieve a draft

    Args:
        draft_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Draft
    """

    return (
        await asyncio_detailed(
            draft_id=draft_id,
            client=client,
        )
    ).parsed
