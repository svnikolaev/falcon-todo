from dataclasses import asdict, dataclass
from datetime import datetime

from falcon_todo.adapters.dto import TodoItem, User


class TodoRepositoryInterface:
    def get(self, user_id: int | None, id: int | None) -> list[TodoItem]: ...

    def add(self, user_id: int, task: str) -> TodoItem | None: ...

    def update(self, id: int, task: str) -> TodoItem | None: ...

    def delete(self, id: int) -> bool | None: ...


class UsersRepositoryInterface:
    def get(self, username: str) -> User | None: ...


@dataclass
class TodoItemService:
    repo: TodoRepositoryInterface
    users_repo: UsersRepositoryInterface

    def get_todo_items(self, username: str) -> list[dict]:
        user = self.users_repo.get(username=username)
        if not user:
            return []

        return [
            {
                **asdict(item),
                'created_at': item.created_at.isoformat()
                if isinstance(item.created_at, datetime)
                else None,
                'updated_at': item.updated_at.isoformat()
                if isinstance(item.updated_at, datetime)
                else None,
            }
            for item in self.repo.get(user_id=user.id)
        ]

    def add_todo_item(self, username: str, task: str):
        user_id = self.users_repo.get(username=username).id
        return self.repo.add(user_id=user_id, task=task)

    def update_todo_item(self, id: int, task: str):
        return self.repo.update(id, task)

    def delete_todo_item(self, id: int):
        return self.repo.delete(id)
