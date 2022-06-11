# api_final_yatube
## Описание
Задача проекта:
Дописать код и привести его в соответствие с документацией: добавить недостающие модели в приложении posts, создать адреса и представления для обработки запросов в приложении api.
## Установка
- Клонирование
```sh
https://github.com/EnTeen/api_final_yatube.git
```
```sh
cd api_final_yatube
```
- Создание виртуального окружения
```sh
python -m venv env
```
```sh
source env/bin/activate
```
```sh
python -m pip install --upgrade pip
```
```sh
Настройка зависимостей из файла requirements.txt
```
- Выполнитье миграции
```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```
- Запустите проект
```sh
python manage.py runserver
```