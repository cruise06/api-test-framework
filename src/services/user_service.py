from typing import Any, Dict, Optional
from src.core.http_client import APIClient

class UserService:
    def __init__(self, client: Optional[APIClient] = None):
        self.client = client or APIClient()

    def get_user(self, user_id: int):
        return self.client.get(f"/users/{user_id}")

    def create_user(self, payload: Dict[str, Any]):
        return self.client.post("/users", json=payload)
