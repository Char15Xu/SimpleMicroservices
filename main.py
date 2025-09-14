from __future__ import annotations

import os
import socket
from datetime import datetime

from typing import Dict, List
from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi import Query, Path
from typing import Optional

from models.course import CourseBase, CourseCreate, CourseRead, CourseUpdate
from models.member import MemberBase, MemberCreate, MemberRead, MemberUpdate

# Set up FastAPI app
port = int(os.environ.get("FASTAPI_PORT", 8000))
app = FastAPI(
    title="Course and Member Management API", 
    version="0.1.0",
    description="API for managing courses and members at a Columbia University using pydantic v2 model and FastAPI."
)

# Database simulation
courses: Dict[UUID, CourseRead] = {}
members: Dict[UUID, MemberRead] = {}

# Course Endpoints
@app.post("/courses", response_model=CourseRead, status_code=201)
def create_course(course: CourseCreate):
    new_course = CourseRead(**course.model_dump())
    courses[new_course.id] = new_course
    print(f"Courses: {courses}")
    return new_course

@app.get("/courses", response_model=List[CourseRead])
def list_course(
    prefix: Optional[str] = Query(None, description="Filter by course prefix"),
    number: Optional[str] = Query(None, description="Filter by course number"),
    title: Optional[str] = Query(None, description="Filter by course title")
):
    results = list(courses.values())
    print(f"Results: {results}")
    if prefix:
        results = [course for course in results if course.prefix == prefix]
    if number:
        results = [course for course in results if course.number == number]
    if title:
        results = [course for course in results if course.title == title]
    return results

@app.get("/courses/{course_id}", response_model=CourseRead)
def get_course(course_id: UUID = Path(..., description="The ID of the course to retrieve")):
    course = courses.get(course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@app.put("/courses/{course_id}", response_model=CourseRead)
def update_course(course_id: UUID, course_update: CourseUpdate):
    existing_course = courses.get(course_id)
    if not existing_course:
        raise HTTPException(status_code=404, detail="Course not found")
    updated_course = existing_course.model_copy(update=course_update.model_dump(exclude_unset=True))
    updated_course.updated_at = datetime.utcnow()
    courses[course_id] = updated_course
    print(f"Courses after update: {courses}")
    return updated_course

from fastapi import HTTPException
from uuid import UUID

@app.delete("/courses/{course_id}", status_code=200)
def delete_course(course_id: UUID):
    course = courses.pop(course_id, None)
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")

    return {"message": f"Course {course.prefix} {course.number} "   f"({course.title}) has been deleted."}


# Members Endpoints
@app.post("/members", response_model=MemberRead, status_code=201)
def create_member(member: MemberCreate):
    new_member = MemberRead(**member.model_dump())
    members[new_member.id] = new_member
    return new_member

@app.get("/members", response_model=List[MemberRead])
def get_members(
    uni: Optional[str] = Query(None, description="Filter by UNI"),
    first_name: Optional[str] = Query(None, description="Filter by first name"),
    last_name: Optional[str] = Query(None, description="Filter by last name"),
    email: Optional[str] = Query(None, description="Filter by email"),
    role: Optional[str] = Query(None, description="Filter by role")
):
    results = list(members.values())
    if uni:
        results = [member for member in results if member.uni == uni]
    if first_name:
        results = [member for member in results if member.first_name == first_name]
    if last_name:
        results = [member for member in results if member.last_name == last_name]
    if email:
        results = [member for member in results if member.email == email]
    if role:
        results = [member for member in results if member.role == role]
    return results

@app.get("/members/{member_id}", response_model=MemberRead)
def get_member(member_id: UUID):
    if member_id not in members:
        raise HTTPException(status_code=404, detail="Member not found")
    return members[member_id]

@app.put("/members/{member_id}", response_model=MemberRead)
def update_member(member_id: UUID, member_update: MemberUpdate):
    existing_member = members.get(member_id)
    if not existing_member:
        raise HTTPException(status_code=404, detail="Member not found")
    updated_member = existing_member.model_copy(update=member_update.model_dump(exclude_unset=True))
    updated_member.updated_at = datetime.utcnow()
    members[member_id] = updated_member
    return updated_member

@app.delete("/members/{member_id}", status_code=200)
def delete_member(member_id: UUID):
    member = members.pop(member_id, None)
    if member is None:
        raise HTTPException(status_code=404, detail="Member not found")
    return {
        "message": f"Member {member.first_name} {member.last_name} has been deleted."
    }

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)