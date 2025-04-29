import falcon
from models import TodoItem, db_init
from playhouse.shortcuts import model_to_dict
import json

# Ресурс для одной задачи
class TodoItemResource:
    def on_get(self, req, resp, item_id):
        try:
            todo_item = TodoItem.get(TodoItem.id == item_id)
            resp.body = json.dumps(model_to_dict(todo_item))
        except TodoItem.DoesNotExist:
            resp.status = falcon.HTTP_404

    def on_put(self, req, resp, item_id):
        data = req.media
        updated_count = (
            TodoItem.update(**data)
                .where(TodoItem.id == item_id)
                .execute()
        )
        if updated_count == 0:
            raise falcon.HTTPNotFound()
        else:
            resp.status = falcon.HTTP_OK

    def on_delete(self, req, resp, item_id):
        deleted_count = TodoItem.delete().where(TodoItem.id == item_id).execute()
        if deleted_count == 0:
            raise falcon.HTTPNotFound()
        else:
            resp.status = falcon.HTTP_NO_CONTENT

# Ресурс для всего списка задач
class TodoListResource:
    def on_get(self, req, resp):
        todos = TodoItem.select().order_by(TodoItem.created_at.desc())
        resp.body = json.dumps([model_to_dict(t) for t in todos])

    def on_post(self, req, resp):
        new_todo = TodoItem.create(**req.media)
        resp.body = json.dumps(model_to_dict(new_todo))
        resp.status = falcon.HTTP_CREATED

# Инициализируем базу данных
db_init()

# Добавляем ресурсы в API
api = falcon.API()
todos = TodoListResource()
item = TodoItemResource()
api.add_route('/todos/', todos)
api.add_route('/todos/{item_id}', item)
