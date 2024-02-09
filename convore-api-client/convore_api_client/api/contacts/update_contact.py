from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contact import Contact
from ...models.update_contact_request import UpdateContactRequest
from ...types import Response


def _get_kwargs(
    contact_id: str,
    *,
    body: UpdateContactRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/contacts/{contact_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Contact]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Contact.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Contact]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateContactRequest,
) -> Response[Contact]:
    """Update a contact

    Args:
        contact_id (str):
        body (UpdateContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Contact]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateContactRequest,
) -> Optional[Contact]:
    """Update a contact

    Args:
        contact_id (str):
        body (UpdateContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Contact
    """

    return sync_detailed(
        contact_id=contact_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateContactRequest,
) -> Response[Contact]:
    """Update a contact

    Args:
        contact_id (str):
        body (UpdateContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Contact]
    """

    kwargs = _get_kwargs(
        contact_id=contact_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    contact_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateContactRequest,
) -> Optional[Contact]:
    """Update a contact

    Args:
        contact_id (str):
        body (UpdateContactRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Contact
    """

    return (
        await asyncio_detailed(
            contact_id=contact_id,
            client=client,
            body=body,
        )
    ).parsed
