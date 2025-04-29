from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    email: str
    password_hash: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class Role:
    id: int
    name: str
    is_admin: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class UserRole:
    id: int
    user: User
    role: Role
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class TodoItem:
    id: int
    note: str
    user_id: int
    completed: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None
