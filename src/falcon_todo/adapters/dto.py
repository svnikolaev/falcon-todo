from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    email: str
    is_active: bool = True
    password_hash: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class Role:
    id: int
    name: str
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class UserRole:
    id: int
    user: User
    role: Role
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None


@dataclass
class TodoItem:
    id: int
    task: str
    user_id: int
    completed: bool = False
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None
