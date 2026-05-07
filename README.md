# 📱 Bi Bi — Сервис для бьюти-мастеров и клиентов

**Bi Bi** — это мобильное приложение, которое помогает бьюти-мастерам находить клиентов, а пользователям — записываться на качественные услуги. Данный репозиторий содержит исходный код Backend-части на Python.

## 🚀 Технологический стек

* **Framework:** [FastAPI](https://fastapi.tiangolo.com/) (Асинхронный бэкенд)
* **Database:** [PostgreSQL](https://www.postgresql.org/) (Хостинг на Neon DB)
* **ORM:** [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (Async Mode)
* **Validation:** [Pydantic v2](https://docs.pydantic.dev/)
* **Environment:** Python 3.9+



📦 Быстрый старт

1. Клонирование репозитория
git clone [https://github.com/ВАШ_ЛОГИН/beauty_marketplace_api.git](https://github.com/ВАШ_ЛОГИН/beauty_marketplace_api.git)
cd beauty_marketplace_api

2. Настройка виртуального окружения
python -m venv venv
# Для Windows:
venv\Scripts\activate
# Для Mac/Linux:
source venv/bin/activate

3. Установка зависимостей
pip install -r requirements.txt

4. Конфигурация (Environment)
Создайте файл .env в корне проекта и добавьте строку подключения к вашей базе данных Neon:
DATABASE_URL=postgresql+asyncpg://user:password@host/dbname
Примечание: убедитесь, что в базе включен SSL (в коде database.py уже прописан connect_args={"ssl": True}).

5. Запуск сервера
uvicorn app.main:app --reload