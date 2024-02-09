from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attachment import Attachment
from ...models.upload_attachment_body import UploadAttachmentBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: UploadAttachmentBody,
    draft_id: Union[Unset, str] = UNSET,
    message_id: Union[Unset, str] = UNSET,
    is_inline: bool,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["draft_id"] = draft_id

    params["message_id"] = message_id

    params["is_inline"] = is_inline

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/v1/attachments",
        "params": params,
    }

    _body = body.to_multipart()

    _kwargs["files"] = _body

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Attachment]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Attachment.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Attachment]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadAttachmentBody,
    draft_id: Union[Unset, str] = UNSET,
    message_id: Union[Unset, str] = UNSET,
    is_inline: bool,
) -> Response[Attachment]:
    """Upload an attachment

    Args:
        draft_id (Union[Unset, str]):
        message_id (Union[Unset, str]):
        is_inline (bool):
        body (UploadAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attachment]
    """

    kwargs = _get_kwargs(
        body=body,
        draft_id=draft_id,
        message_id=message_id,
        is_inline=is_inline,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadAttachmentBody,
    draft_id: Union[Unset, str] = UNSET,
    message_id: Union[Unset, str] = UNSET,
    is_inline: bool,
) -> Optional[Attachment]:
    """Upload an attachment

    Args:
        draft_id (Union[Unset, str]):
        message_id (Union[Unset, str]):
        is_inline (bool):
        body (UploadAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attachment
    """

    return sync_detailed(
        client=client,
        body=body,
        draft_id=draft_id,
        message_id=message_id,
        is_inline=is_inline,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadAttachmentBody,
    draft_id: Union[Unset, str] = UNSET,
    message_id: Union[Unset, str] = UNSET,
    is_inline: bool,
) -> Response[Attachment]:
    """Upload an attachment

    Args:
        draft_id (Union[Unset, str]):
        message_id (Union[Unset, str]):
        is_inline (bool):
        body (UploadAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Attachment]
    """

    kwargs = _get_kwargs(
        body=body,
        draft_id=draft_id,
        message_id=message_id,
        is_inline=is_inline,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: UploadAttachmentBody,
    draft_id: Union[Unset, str] = UNSET,
    message_id: Union[Unset, str] = UNSET,
    is_inline: bool,
) -> Optional[Attachment]:
    """Upload an attachment

    Args:
        draft_id (Union[Unset, str]):
        message_id (Union[Unset, str]):
        is_inline (bool):
        body (UploadAttachmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Attachment
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            draft_id=draft_id,
            message_id=message_id,
            is_inline=is_inline,
        )
    ).parsed
