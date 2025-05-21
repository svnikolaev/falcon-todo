# Readme

## Migrations

`pip install yoyo-migrations`
`yoyo init --database sqlite:///db.sqlite src/db/migrations/`
`yoyo new --sql -m "Initial"`

`yoyyo.ini`:

```ini
[DEFAULT]
sources = src/falcon_todo/database/migrations/
database = sqlite:///db.sqlite
batch_mode = off
verbosity = 0
```

## Run

```shell
kasamy@DESKTOP-O7VDCLQ /mnt/d/dev_local/study/falcon-todo (dev) 
❯ cd src
kasamy@DESKTOP-O7VDCLQ /mnt/d/dev_local/study/falcon-todo/src (dev) 
❯ uv run -m falcon_todo.composites.api
Serving on http://127.0.0.1:8000 ...
```
