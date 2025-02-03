from abc import ABC, abstractmethod
from typing import Literal

import aiohttp

from .errors import BadRequestError, UnauthorizedError, ForbiddenError


class BaseHttpExecutor(ABC):
    def __init__(
        self,
        headers: dict
    ):
        self.__headers = headers
    
    async def make_request(
        self,
        url: str,
        method: Literal["get", "post"] = "post",
        load_response_body: bool = True,
        **kwargs
    ) -> (aiohttp.ClientResponse, dict):
        async with aiohttp.ClientSession() as session:
            async with getattr(session, method)(
                url=url,
                headers=self.__headers,
                **kwargs
            ) as resp:
                if resp.status == 404:
                    raise BadRequestError(f"The requested {url=} not found. Check API updates.")
                
                resp_body = await resp.json()
                
                self._check_response_status(resp, resp_body)
                
                return resp, resp_body if load_response_body else {}
    
    @abstractmethod
    def _check_response_status(self, response: aiohttp.ClientResponse, response_body: dict) -> None:
        raise NotImplementedError


class CryptoCloudHttpExecutor(BaseHttpExecutor):
    def _check_response_status(self, response: aiohttp.ClientResponse, response_body: dict) -> None:
        resp_code = response.status
        
        match resp_code:
            case 400:
                raise BadRequestError(self._format_error(resp_code, response_body.get("result")))
            case 401:
                raise UnauthorizedError(self._format_error(resp_code, response_body.get("detail")))
            case 403:
                raise ForbiddenError(self._format_error(resp_code, response_body.get("detail")))
    
    @staticmethod
    def _format_error(code: int, tip: str) -> str:
        text = f"Returned [{code}] error because - '{tip}'. " \
               "Make sure that creds and params was correctly passed."
        
        return text
