from __future__ import annotations

from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from pydantic import BaseModel, Field

class MemberBase(BaseModel):
    uni: str = Field(
        ...,
        description="Member's Columbia University UNI.",
        json_schema_extra={"example": "cx1234"},
    ) 
    first_name: str = Field(
        ...,
        description="Member's first name.",
        json_schema_extra={"example": "Charles"},
    )
    last_name: str = Field(
        ...,
        description="Member's last name.",
        json_schema_extra={"example": "Xu"},
    )
    email: Optional[str] = Field(
        ...,
        description="Member's email address.",
        json_schema_extra={"example": "cx1234@columbia.edu"},
    )
    role: Optional[str] = Field(
        ...,
        description="Member's role.",
        json_schema_extra={"example": "student"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "uni": "cx1234",
                    "first_name": "Charles",
                    "last_name": "Xu",
                    "email": "cx1234@columbia.edu",
                    "role": "student",
                }
            ]
        }
    }

class MemberCreate(MemberBase):
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "uni": "cx1234",
                    "first_name": "Charles",
                    "last_name": "Xu",
                    "email": "cx1234@columbia.edu",
                    "role": "student",
                }
            ]
        }
    }   

class MemberRead(MemberBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "uni": "cx1234",
                    "first_name": "Charles",
                    "last_name": "Xu",
                    "email": "cx1234@columbia.edu",
                    "role": "student",
                    "created_at": datetime.utcnow().isoformat(),
                    "updated_at": datetime.utcnow().isoformat()
                }
            ]
        }
    }

class MemberUpdate(BaseModel):
    uni: Optional[str] = Field(
        None,
        description="Member's Columbia University UNI.",
        json_schema_extra={"example": "cx1234"},
    )
    first_name: Optional[str] = Field(
        None,
        description="Member's first name.",
        json_schema_extra={"example": "Charles"},
    )
    last_name: Optional[str] = Field(
        None,
        description="Member's last name.",
        json_schema_extra={"example": "Xu"},
    )
    email: Optional[str] = Field(
        None,
        description="Member's email address.",
        json_schema_extra={"example": "cx1234@columbia.edu"},   
    )
    role: Optional[str] = Field(
        None,
        description="Member's role.",
        json_schema_extra={"example": "student"},
    )

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": str(uuid4()),
                    "uni": "cx1234",
                    "first_name": "Charles",
                    "last_name": "Xu",
                    "email": "cx1234@columbia.edu",
                    "role": "student",
                }
            ]
        }
    }
