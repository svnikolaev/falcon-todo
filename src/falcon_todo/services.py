from adapters.dto import TodoItem, User
from dataclasses import dataclass


class TodoRepositoryInterface:
    def get(self, user_id: str | None, id: int | None) -> list[TodoItem]: ...

    def add(self, user_id: str, task: str) -> TodoItem | None: ...

    def update(self, id: int, task: str) -> TodoItem | None: ...

    def delete(self, id: int) -> bool | None: ...


class UsersRepositoryInterface:
    def get(self, username: str) -> User: ...


@dataclass
class TodoItemService:
    todo_repo: TodoRepositoryInterface
    users_repo: UsersRepositoryInterface

    def get_todo_items(self, username: str):
        user_id = self.users_repo.get(username=username).id
        return self.repo.get(user_id=user_id)

    def add_todo_item(self, username: str, task: str):
        user_id = self.users_repo.get(username=username).id
        return self.repo.add(user_id=user_id, task=task)

    def update_todo_item(self, id: int, task: str):
        return self.repo.update(id, task)

    def delete_todo_item(self, id: int):
        return self.repo.delete(id)
