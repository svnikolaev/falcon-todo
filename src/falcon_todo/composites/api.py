from wsgiref.simple_server import make_server

import falcon

from falcon_todo.adapters import repositories as repo
from falcon_todo.adapters import resources as res
from falcon_todo.application import services as svc

# from falcon_todo.settings import DB
import logging

logger = logging.getLogger('composites.api')
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] %(name)s:%(lineno)s | %(message)s',
    level=logging.DEBUG,
    handlers=[logging.StreamHandler()],
)


def build_app():
    todo_repo = repo.DictTodoRepo(data=repo.TODO_DATA)
    users_repo = repo.DictUserRepo(data=repo.USERS_DATA)
    todo_item_resource = res.TodoItemResource(
        svc.TodoItemService(
            repo=todo_repo,
            users_repo=users_repo,
        ),
    )
    app = res.create_app(todo_item_resource=todo_item_resource)
    return app


def start_dev_server(
    app: falcon.App, host: str = '127.0.0.1', port: int = 8000
):
    with make_server(host, port, app) as httpd:
        print(f'Serving on http://{host}:{port} ...')
        httpd.serve_forever()


if __name__ == '__main__':
    app = build_app()
    start_dev_server(app=app)
