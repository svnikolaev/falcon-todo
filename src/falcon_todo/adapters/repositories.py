from datetime import datetime

from falcon_todo.adapters.dto import TodoItem, User

TODO_DATA = {
    1: TodoItem(id=1, task='Complete initial setup', user_id=1, is_active=True),
    2: TodoItem(id=2, task='Review database schema', user_id=2, is_active=True),
    3: TodoItem(id=3, task='Test API endpoints', user_id=3, is_active=True),
    4: TodoItem(id=4, task='Configure user roles', user_id=1, is_active=True),
    5: TodoItem(id=5, task='Implement auth', user_id=2, is_active=True),
    6: TodoItem(id=6, task='Setup CI/CD pipeline', user_id=3, is_active=True),
}
USERS_DATA = {
    1: User(id=1, username='admin', email='admin@example.com', is_active=True),
    2: User(id=2, username='user1', email='user1@example.com', is_active=True),
    3: User(id=3, username='user2', email='user2@example.com', is_active=True),
}


class DictTodoRepo:
    _data: dict[int, TodoItem] = {}
    _id: int = 0

    def __init__(self, data: dict[int, TodoItem] | None = None):
        if data:
            self._data = data
        if self._data.keys():
            self._id = max(self._data.keys())

    def get(
        self, user_id: int | None = None, id: int | None = None
    ) -> list[TodoItem]:
        if id:
            todo_item = self._data.get(id)
            if not todo_item or not todo_item.is_active:
                return []
            return [todo_item]
        elif user_id:
            return [
                item
                for item in self._data.values()
                if (item.user_id == user_id and item.is_active)
            ]
        else:
            return []

    def add(self, user_id: int, task: str) -> TodoItem | None:
        self._id += 1
        self._data[self._id] = TodoItem(
            id=self._id,
            user_id=user_id,
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
        self._data[id] = item
        return item

    def delete(self, id: int) -> bool:
        item = self.get(id)
        if not item:
            return False
        self._data[id]['is_active'] = False
        return True


class DictUserRepo:
    _data: dict[int, User] = {}
    _id: int = 0

    def __init__(self, data: dict[int, User] | None = None):
        if data:
            self._data = data
        if self._data.keys():
            self._id = max(self._data.keys())

    def get(self, username: str) -> User | None:
        users = [
            user for user in self._data.values() if user.username == username
        ]
        return None if not users else users[0]


class TodoRepo:
    def __init__(self, connection):
        self._connection = connection

    def get(
        self, id: int | None = None
    ) -> list[TodoItem] | TodoItem | None: ...

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

    def get(self, username: str): ...
