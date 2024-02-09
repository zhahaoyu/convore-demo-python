from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.connector import Connector
from ...models.update_connector_request import UpdateConnectorRequest
from ...types import Response


def _get_kwargs(
    connector_id: str,
    *,
    body: UpdateConnectorRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/connectors/{connector_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Connector]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Connector.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Connector]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateConnectorRequest,
) -> Response[Connector]:
    """Update a connector

    Args:
        connector_id (str):
        body (UpdateConnectorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Connector]
    """

    kwargs = _get_kwargs(
        connector_id=connector_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateConnectorRequest,
) -> Optional[Connector]:
    """Update a connector

    Args:
        connector_id (str):
        body (UpdateConnectorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Connector
    """

    return sync_detailed(
        connector_id=connector_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateConnectorRequest,
) -> Response[Connector]:
    """Update a connector

    Args:
        connector_id (str):
        body (UpdateConnectorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Connector]
    """

    kwargs = _get_kwargs(
        connector_id=connector_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    connector_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateConnectorRequest,
) -> Optional[Connector]:
    """Update a connector

    Args:
        connector_id (str):
        body (UpdateConnectorRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Connector
    """

    return (
        await asyncio_detailed(
            connector_id=connector_id,
            client=client,
            body=body,
        )
    ).parsed
