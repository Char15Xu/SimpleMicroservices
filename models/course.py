from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field


class CourseBase(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    prefix: str = Field(
        ...,
        description="Course's department prefix, e.g., COMS",
        json_schema_extra={"example": "COMS"},
        )
    number: str = Field(
        ..., 
        description="Course number, e.g., 4153",
        json_schema_extra={"example": "4153"},
        )
    title: str = Field(
        ...,
        description="Course title",
        json_schema_extra={"example": "Cloud Computing"},
        )
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "prefix": "COMS",
                    "number": "4153",
                    "title": "Cloud Computing"
                }
            ]
        }
    }

class CourseCreate(CourseBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "prefix": "COMS",
                    "number": "4153",
                    "title": "Cloud Computing"
                }
            ]
        }
    }

class CourseRead(CourseBase):
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "prefix": "COMS",
                    "number": "4153",
                    "title": "Cloud Computing",
                    "created_at": datetime.utcnow().isoformat(),
                    "updated_at": datetime.utcnow().isoformat()
                }
            ]
        }
    }
    
class CourseUpdate(BaseModel):
    prefix: Optional[str] = Field(
        None,
        description="Course's department prefix, e.g., COMS",
        json_schema_extra={"example": "COMS"},
        )
    number: Optional[str] = Field(
        None, 
        description="Course number, e.g., 4153",
        json_schema_extra={"example": "4153"},
        )
    title: Optional[str] = Field(
        None,
        description="Course title",
        json_schema_extra={"example": "Cloud Computing"},
        )
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "prefix": "COMS",
                    "number": "4153",
                    "title": "Cloud Computing"
                }
            ]
        }
    }

