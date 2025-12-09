from pathlib import Path
import json
import yaml
from typing import Any

def load_yaml(path: str | Path) -> Any:
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_json(path: str | Path) -> Any:
    path = Path(path)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
