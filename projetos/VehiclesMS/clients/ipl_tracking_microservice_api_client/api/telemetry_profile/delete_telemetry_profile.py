from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    telemetryprofile_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/telemetryprofiles/{telemetryprofileId}".format(client.base_url, telemetryprofileId=telemetryprofile_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, ErrorResponse]]:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    telemetryprofile_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse]]:
    """Delete TelemetryProfile

     This operation is delete a TelemetryProfile.

    Args:
        telemetryprofile_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        telemetryprofile_id=telemetryprofile_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    telemetryprofile_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ErrorResponse]]:
    """Delete TelemetryProfile

     This operation is delete a TelemetryProfile.

    Args:
        telemetryprofile_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return sync_detailed(
        telemetryprofile_id=telemetryprofile_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    telemetryprofile_id: str,
    *,
    client: Client,
) -> Response[Union[Any, ErrorResponse]]:
    """Delete TelemetryProfile

     This operation is delete a TelemetryProfile.

    Args:
        telemetryprofile_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        telemetryprofile_id=telemetryprofile_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    telemetryprofile_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, ErrorResponse]]:
    """Delete TelemetryProfile

     This operation is delete a TelemetryProfile.

    Args:
        telemetryprofile_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ErrorResponse]]
    """

    return (
        await asyncio_detailed(
            telemetryprofile_id=telemetryprofile_id,
            client=client,
        )
    ).parsed
