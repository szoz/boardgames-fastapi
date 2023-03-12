# boardgames-fastapi

## Setup

* Create virtual environment and install project dependencies using
  [pipenv](https://pipenv.pypa.io/en/latest/install/#installing-packages-for-your-project):

  `pipenv install`

## Usage

* Run application:

  `pipenv run uvicorn src.main:app`

## Contributing

Follow [architecture guidelines](https://github.com/zhanymkanov/fastapi-best-practices) applied in this project.

## Database

Initial DB creation schema:

```sql
create table games
(
    id          integer PRIMARY KEY NOT NULL,
    title       varchar(100) UNIQUE,
    year        integer,
    url         varchar(100),
    description text
);
```
