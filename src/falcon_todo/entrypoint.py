from wsgiref.simple_server import make_server

from falcon_todo.adapters.api import create_app
from falcon_todo.settings import DB


def start_dev_server(
    host: str = '127.0.0.1',
    port: int = 8000
):
    app = create_app()
    with make_server(host, port, app) as httpd:
        print(f'Serving on http://{host}:{port} ...')
        httpd.serve_forever()


if __name__ == "__main__":
    start_dev_server()
