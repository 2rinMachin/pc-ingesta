import json
import os
from decimal import Decimal

PROJECT_NAME = os.environ["PROJECT_NAME"]
STAGE = os.environ["STAGE"]


def resource_name(basename: str) -> str:
    return f"{PROJECT_NAME}-{STAGE}-{basename}"


def json_default(obj: dict):
    if isinstance(obj, Decimal):
        return float(obj)

    raise TypeError


def to_json(obj: dict):
    return json.dumps(obj, default=json_default)
