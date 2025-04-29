# Readme

## Migrations

`pip install yoyo-migrations`
`yoyo init --database sqlite:///db.sqlite src/db/migrations/`
`yoyo new --sql -m "Initial"`

`yoyyo.ini`
```ini
[DEFAULT]
sources = src/falcon_todo/db/migrations/
database = sqlite:///db.sqlite
batch_mode = off
verbosity = 0
```
