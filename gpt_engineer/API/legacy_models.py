# generated by fastapi-codegen:
#   filename:  openapi.yml
#   timestamp: 2023-09-16T00:59:36+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field

import datetime


class NotFoundResponse(BaseModel):
    message: str = Field(
        ...,
        description="Message stating the entity was not found",
        example="Unable to find entity with the provided id",
    )

class Status(Enum):
    created = "created"
    running = "running"
    completed = "completed"

