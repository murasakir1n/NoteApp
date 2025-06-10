# Notes App 

Простое приложение для создания заметок на Django с авторизацией 

## Описание

Это веб-приложение, где можно:
- Создавать и просматривать заметки
- Регистрироваться и входить в аккаунт
- Редактировать и удалять заметки
- Простматривать личный профиль с заметками

## Технологии 

-Python 
-Django 
-Django REST Framework (DRF)
-HTML / CSS
-Bootstrap 5 
-Git / GitHub

## Установка

1. Клонируйте репозиторий
   git clone https://github.com/murasakir1n/NoteApp

2. Установите зависимости
   pip install -r requirements.txt

3. Примените миграции
   python manage.py migrate

4. Запустите сервер
   python manage.py runserver

5. Перейдите по адресу:
http://127.0.0.1:8000/

## API

- GET /api/notes/ — получить все заметки
- POST /api/notes/ — добавить новую заметку

## Автор

murasakir1n · GitHub: [@murasakir1n](https://github.com/murasakir1n) 
