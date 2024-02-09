from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.label import Label
from ...models.update_label_request import UpdateLabelRequest
from ...types import Response


def _get_kwargs(
    label_id: str,
    *,
    body: UpdateLabelRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "patch",
        "url": f"/v1/labels/{label_id}",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Label]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Label.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Label]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    label_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLabelRequest,
) -> Response[Label]:
    """Update a label

    Args:
        label_id (str):
        body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Label]
    """

    kwargs = _get_kwargs(
        label_id=label_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    label_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLabelRequest,
) -> Optional[Label]:
    """Update a label

    Args:
        label_id (str):
        body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Label
    """

    return sync_detailed(
        label_id=label_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    label_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLabelRequest,
) -> Response[Label]:
    """Update a label

    Args:
        label_id (str):
        body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Label]
    """

    kwargs = _get_kwargs(
        label_id=label_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    label_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateLabelRequest,
) -> Optional[Label]:
    """Update a label

    Args:
        label_id (str):
        body (UpdateLabelRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Label
    """

    return (
        await asyncio_detailed(
            label_id=label_id,
            client=client,
            body=body,
        )
    ).parsed
