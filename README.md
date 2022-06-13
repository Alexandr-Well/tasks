## Установка и запуск

1. Склонировать репозиторий с Github:
```
git clone https://github.com/Alexandr-Well/tasks.git
```

2. В дирректории проекта создать виртуальное окружение с учетом вашей ОС:

```
python -m venv venv
```

3. Установка зависимостей:
```
pip install -r requirements.txt
```

4. Создать и применить миграции в базу данных:
```
python manage.py migrate
```
5. Запустить сервер
```
python manage.py runserver
```

***
## URLS
***
```
http://127.0.0.1:8000/test_tasks/colors/
http://127.0.0.1:8000/test_tasks/quadratic_eq/

```
***