## FastAPI 

## Change env

```bash
    workon fastapi
```

## Run App

```bash
    uvicorn main:app --reload
```


## Explore 

* Make it compatible for both CLI as well as for REST API

## Initializing Migrations

`alembic init migrations`

## Applying migrtaion after settings up config

`alembic revision --autogenerate -m "add user_id to a task"`

## Change in db

`alembic upgrade head`