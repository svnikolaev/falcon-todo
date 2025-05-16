import logging
import sqlite3
from dataclasses import dataclass
from datetime import datetime

import falcon
from embrace import pool

# from falcon_todo.adapters import dto
from falcon_todo.adapters import repositories as repo
from falcon_todo.application import services as svc

app = falcon.App()


@dataclass
class TodoItemResource:
    todo_items: svc.TodoItemService
    logger: logging.Logger = logging.getLogger(__name__)

    def on_get(self, req: falcon.Request, resp: falcon.Response, username: str):
        self.logger.debug("Received GET request")
        # import pdb; pdb.set_trace()
        if not username:
            resp.status_code = falcon.HTTP_400
            resp.media = {"error": "User not provided"}
        else:
            todo_items = self.todo_items.get_todo_items(username)
            resp.content_type = falcon.MEDIA_JSON
            resp.media = todo_items

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        try:
            task = req.media['task']
        except KeyError:
            resp.status_code = falcon.HTTP_400
            return

        result = self.items_repo.add({'task': task})
        if result:
            resp.status_code = falcon.HTTP_201
        else:
            resp.status_code = falcon.HTTP_400

    def on_update(self, req: falcon.Request, resp: falcon.Response, id: int):
        try:
            task = req.media['task']
        except KeyError:
            resp.status_code = falcon.HTTP_400
            return

    def on_delete(self, req: falcon.Request, resp: falcon.Response, id: int):
        ...


class Homepage:
    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'Hello, Falcon! \n'


def create_app(todo_item_resource: TodoItemResource) -> falcon.App:
    app.add_route('/', Homepage())
    app.add_route('/todo/{username}', todo_item_resource)
    app.add_route('/todo', todo_item_resource)
    return app


# # Ресурс для одной задачи
# class TodoItemResource:
#     def on_get(self, req, resp, item_id):
#         try:
#             todo_item = TodoItem.get(TodoItem.id == item_id)
#             resp.body = json.dumps(model_to_dict(todo_item))
#         except TodoItem.DoesNotExist:
#             resp.status = falcon.HTTP_404

#     def on_put(self, req, resp, item_id):
#         data = req.media
#         updated_count = (
#             TodoItem.update(**data)
#                 .where(TodoItem.id == item_id)
#                 .execute()
#         )
#         if updated_count == 0:
#             raise falcon.HTTPNotFound()
#         else:
#             resp.status = falcon.HTTP_OK

#     def on_delete(self, req, resp, item_id):
#         deleted_count = TodoItem.delete().where(TodoItem.id == item_id).execute()
#         if deleted_count == 0:
#             raise falcon.HTTPNotFound()
#         else:
#             resp.status = falcon.HTTP_NO_CONTENT

# # Ресурс для всего списка задач
# class TodoListResource:
#     def on_get(self, req, resp):
#         todos = TodoItem.select().order_by(TodoItem.created_at.desc())
#         resp.body = json.dumps([model_to_dict(t) for t in todos])

#     def on_post(self, req, resp):
#         new_todo = TodoItem.create(**req.media)
#         resp.body = json.dumps(model_to_dict(new_todo))
#         resp.status = falcon.HTTP_CREATED

# # Инициализируем базу данных
# db_init()

# # Добавляем ресурсы в API
# api = falcon.API()
# todos = TodoListResource()
# item = TodoItemResource()
# api.add_route('/todos/', todos)
# api.add_route('/todos/{item_id}', item)
