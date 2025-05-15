from dataclasses import dataclass
from datetime import datetime
from adapters.dto import TodoItem, User
# from embrace import pool


@dataclass
class TodoItem:
    id: int
    task: str
    user_id: int
    completed: bool = False
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None


class DictTodoRepo():
    _data = {}
    _id = 0

    def __init__(self, data: dict = {}):
        self._data = data

    def get(self, id: int | None = None) -> list[TodoItem] | TodoItem | None:
        if not id:
            return [item for item in self._data.values() if item['is_active']]
        return self._data.get(id)

    def add(self, task: str) -> TodoItem | None:
        self._id += 1
        self._data[self._id] = TodoItem(
            id=self._id,
            user_id=0,
            task=task,
            created_at=datetime.now(tz=datetime.timezone.utc),
            updated_at=datetime.now(tz=datetime.timezone.utc),
        )
        return self._data[self._id]

    def update(self, id: int, task: str) -> TodoItem | None:
        item = self.get(id)
        if not item:
            return
        item['task'] = task
        self._data[id] = task
        return task

    def delete(self, id: int) -> bool:
        item = self.get(id)
        if not item:
            return
        self._data[id]['is_active'] = False
        return True


class DictUserRepo:
    _data = {
        'admin': User()
    }

    def __init__(self, data: dict | None):
        if data:
            self._data = data

    def get(self, username: str) -> User:



class TodoRepo:
    def __init__(self, connection):
        self._connection = connection

    def get(self, id: int | None = None) -> list[TodoItem] | TodoItem | None:
        
        ...

    def add(self, task: str) -> TodoItem | None:
        # self._id += 1
        # self._data[self._id] = TodoItem(
        #     id=self._id,
        #     user_id=0,
        #     task=task,
        #     created_at=datetime.now(tz=datetime.timezone.utc),
        #     updated_at=datetime.now(tz=datetime.timezone.utc),
        # )
        # return self._data[self._id]
        ...

    def update(self, id: int, task: str) -> TodoItem | None:
        # item = self.get(id)
        # if not item:
        #     return
        # item['task'] = task
        # self._data[id] = task
        # return task
        ...

    def delete(self, id: int) -> bool:
        # item = self.get(id)
        # if not item:
        #     return
        # self._data[id]['is_active'] = False
        # return True
        ...


class UserRepo:
    def __init__(self, connection):
        self._connection = connection

    def get(self, username: str):
        ...
