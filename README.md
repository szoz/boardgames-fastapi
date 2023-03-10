# boardgames-fastapi

## Database

Initial DB creation schema:

```sql
create table games
(
    id          integer PRIMARY KEY NOT NULL,
    title       char(100) UNIQUE,
    year        integer,
    url         char(100),
    description text
);
```
