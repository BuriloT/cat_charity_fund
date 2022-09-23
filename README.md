# QRKot

## QRKot - Приложение для Благотворительного фонда поддержки котиков.

> Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с поддержкой кошачьей популяции.

## Технологии проекта

- Python — высокоуровневый язык программирования.
- FastAPI — веб-фреймворк для создания API.
- SQLAlchemy - библиотека для работы с реляционными СУБД.
- Alembic - инструмент для миграции базы данных.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/BuriloT/cat_charity_fund.git
```

```
cd cat_charity_fund
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создайте и заполните файл .env:

```
APP_TITLE=Кошачий благотворительный фонд
APP_DESCRIPTION=Сервис для поддержки котиков!
DATABASE_URL=sqlite+aiosqlite:///./fastapi.db
SECRET=YOUR_SECRET_KEY
FIRST_SUPERUSER_EMAIL=1@mail.ru
FIRST_SUPERUSER_PASSWORD=admin
```

Выполните миграции:

```
alembic upgrade head
```

Запустите проект:

```
uvicorn app.main:app --reload
```

## Примеры запросов:

POST-запрос на создание благотворительного проекта.

```
http://127.0.0.1:8000/charity_project/
```

Request:

```
{
  "name": "string",
  "description": "string",
  "full_amount": 0
}
```

GET-запрос на получение списока всех пожертвований.

```
http://127.0.0.1:8000/donation/
```

Successful response:

```
[
  {
    "full_amount": 0,
    "comment": "string",
    "id": 0,
    "create_date": "2019-08-24T14:15:22Z",
    "user_id": "string",
    "invested_amount": 0,
    "fully_invested": true,
    "close_date": "2019-08-24T14:15:22Z"
  }
]
```

Остальные запросы можно посмотреть в документации проекта, файл openapi.json.
