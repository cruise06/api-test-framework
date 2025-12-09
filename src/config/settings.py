from pathlib import Path
import os
import yaml
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parents[2]   # -> 项目根/src 的上两级
ENV_DIR = BASE_DIR / "src" / "config" / "envs"

class EnvConfig(BaseModel):
    base_url: str
    timeout: int
    env_name: str

def load_config(env: str | None = None) -> EnvConfig:
    env = env or os.getenv("ENV", "dev")
    file_path = ENV_DIR / f"{env}.yaml"
    if not file_path.exists():
        raise FileNotFoundError(f"Config file not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return EnvConfig(**data)

settings = load_config()
