import logging
from dataclasses import dataclass

import falcon

from falcon_todo.application import services as svc


@dataclass
class TodoItemResource:
    todo_service: svc.TodoItemService
    logger: logging.Logger = logging.getLogger(__name__)

    def on_get(self, req: falcon.Request, resp: falcon.Response):
        self.logger.debug('Received GET request')
        username = req.get_header('username')
        if not username:
            resp.status_code = falcon.HTTP_400
            resp.media = {'error': 'User not provided'}
        else:
            todo_items = self.todo_service.get_todo_items(username)
            resp.content_type = falcon.MEDIA_JSON
            resp.media = todo_items

    def on_post(self, req: falcon.Request, resp: falcon.Response):
        self.logger.debug('Received POST request')
        data = req.media
        if 'task' not in data or 'username' not in data:
            self.logger.debug('Missing required fields: task, username')
            resp.status_code = falcon.HTTP_400
            return
        result = self.todo_service.add_todo_item(
            username=data['username'],
            task=data['task'],
        )
        if result:
            resp.status_code = falcon.HTTP_201
        else:
            resp.status_code = falcon.HTTP_400

    def on_patch(self, req: falcon.Request, resp: falcon.Response):
        self.logger.debug('Received UPDATE request')
        data = req.media
        if 'id' not in data or 'task' not in data:
            resp.status_code = falcon.HTTP_400
            return
        try:
            item_id = int(data['id'])
        except ValueError:
            self.logger.debug('Invalid id format')
            resp.status = falcon.HTTP_400
            return
        task = data['task']
        result = self.todo_service.update_todo_item(id=item_id, task=task)
        if result:
            resp.status_code = falcon.HTTP_200
        else:
            resp.status_code = falcon.HTTP_404

    def on_delete(self, req: falcon.Request, resp: falcon.Response):
        self.logger.debug('Received DELETE request')
        data = req.media
        if 'id' not in data:
            self.logger.debug('Missing id in request data')
            resp.status = falcon.HTTP_400
            return
        try:
            item_id = int(data['id'])
        except ValueError:
            self.logger.debug('Invalid id format')
            resp.status = falcon.HTTP_400
            return
        result = self.todo_service.delete_todo_item(id=item_id)
        if result:
            resp.status_code = falcon.HTTP_204
        else:
            self.logger.debug('Todo item not found')
            resp.status_code = falcon.HTTP_404


class Homepage:
    def on_get(self, req, resp):
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = 'Hello, Falcon! \n'


def create_app(
    todo_item_resource: TodoItemResource,
    allow_origins: str = '*',
    logger: logging.Logger = logging.getLogger(__name__),
) -> falcon.App:
    logger.info('Creating API app')
    app = falcon.App(
        middleware=falcon.CORSMiddleware(
            allow_origins=allow_origins,
        )
    )
    app.add_route('/', Homepage())
    app.add_route('/todo', todo_item_resource)
    return app
