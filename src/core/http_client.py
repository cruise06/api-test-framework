import httpx
from typing import Any, Dict, Optional
from src.config.settings import settings
from src.core.logger import get_logger

logger = get_logger("http_client")

class APIClient:
    def __init__(
        self,
        base_url: Optional[str] = None,
        timeout: Optional[int] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        self.base_url = base_url or settings.base_url
        self.timeout = timeout or settings.timeout
        self._client = httpx.Client(
            base_url=self.base_url,
            timeout=self.timeout,
            headers=headers or {},
        )

    def request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> httpx.Response:
        logger.info(f"{method.upper()} {url}")
        return self._client.request(
            method=method.upper(),
            url=url,
            params=params,
            json=json,
            headers=headers,
        )

    def get(self, url: str, **kwargs) -> httpx.Response:
        return self.request("GET", url, **kwargs)

    def post(self, url: str, **kwargs) -> httpx.Response:
        return self.request("POST", url, **kwargs)

    def close(self):
        self._client.close()
