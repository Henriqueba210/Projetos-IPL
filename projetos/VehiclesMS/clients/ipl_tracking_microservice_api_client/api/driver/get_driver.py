from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.error_response import ErrorResponse
from ...models.get_driver_response import GetDriverResponse
from ...types import Response


def _get_kwargs(
    driver_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/drivers/{driverId}".format(client.base_url, driverId=driver_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[ErrorResponse, GetDriverResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = GetDriverResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[ErrorResponse, GetDriverResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    driver_id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, GetDriverResponse]]:
    """Get a single Driver's info

     This operation is used to retrieve the details of a specific device.

    Args:
        driver_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetDriverResponse]]
    """

    kwargs = _get_kwargs(
        driver_id=driver_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    driver_id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, GetDriverResponse]]:
    """Get a single Driver's info

     This operation is used to retrieve the details of a specific device.

    Args:
        driver_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetDriverResponse]]
    """

    return sync_detailed(
        driver_id=driver_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    driver_id: str,
    *,
    client: Client,
) -> Response[Union[ErrorResponse, GetDriverResponse]]:
    """Get a single Driver's info

     This operation is used to retrieve the details of a specific device.

    Args:
        driver_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetDriverResponse]]
    """

    kwargs = _get_kwargs(
        driver_id=driver_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    driver_id: str,
    *,
    client: Client,
) -> Optional[Union[ErrorResponse, GetDriverResponse]]:
    """Get a single Driver's info

     This operation is used to retrieve the details of a specific device.

    Args:
        driver_id (str):  Example: 0af401df-7d7a-1f36-817d-7b0a058d0003.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetDriverResponse]]
    """

    return (
        await asyncio_detailed(
            driver_id=driver_id,
            client=client,
        )
    ).parsed
