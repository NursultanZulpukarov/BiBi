# 📱 Bi Bi — Сервис для бьюти-мастеров и клиентов

**Bi Bi** — это мобильное приложение, которое помогает бьюти-мастерам находить клиентов, а пользователям — записываться на качественные услуги. Данный репозиторий содержит исходный код Backend-части на Python.

## 🚀 Технологический стек

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Асинхронный бэкенд)
* **Database:** [PostgreSQL](https://www.postgresql.org/) (Хостинг на Neon DB)
* **ORM:** [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (Async Mode)
* **Validation:** [Pydantic v2](https://docs.pydantic.dev/)
* **Environment:** Python 3.9+

---

## 🛠 Архитектура проекта

```text
app/
├── main.py          # Точка входа, настройка эндпоинтов и CORS
├── database.py      # Подключение к БД и настройка сессий
├── models.py        # SQLAlchemy модели (таблицы masters и services)
├── schemas.py       # Pydantic схемы для валидации запросов/ответов
└── crud.py          # Логика работы с базой данных