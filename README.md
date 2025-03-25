*Выполнено во время прохождения [конкурса](https://t.me/hexlet_ru/5883) от Хекслета.* `2024-12-09/2024-12-15`

# Hexlet_2
Это API на основе Django для управления генетическими тестами и анализа статистики.

## О проекте
Проект предоставляет интерфейс для работы с генетическими тестами, включая их просмотр, добавление новых данных и анализ статистики. 
API разработан с использованием Django REST Framework, а для автоматической документации используется **drf-spectacular**.

## Основные возможности
- Просмотр списка генетических тестов, включая фильтрацию по видам.
- Внесение новых данных о генетических тестах.
- Агрегированный анализ данных тестов.

## Технологии
- Django
- Django REST Framework
- django-filter
- django-environ
- PostgreSQL
- drf-spectacular

## Документация API
Автоматически сгенерированная спецификация API доступна в формате OpenAPI.

## Структура проекта
- api/ — маршруты API и документация.
- config/ — настройки проекта и базовая конфигурация URL.
- genetic_test/ — бизнес-логика для работы с генетическими тестами.

## Установка и настройка
1. Клонирование репозитория:
`git clone https://github.com/Animatrees/Hexlet_2.git`
2. Установка зависимостей:  
   (_убедитесь, что у вас установлен Poetry_)   
`poetry install`
3. Создание .env файла:  
Скопируйте пример конфигурации `.env.example` в `.env` файл.  
Отредактируйте `.env` в соответствии с вашими настройками.
4. Применение миграций
`python manage.py migrate`
5. Создание тестовых данных
`python manage.py create_test_data`
6. Запуск сервера разработки
`python manage.py runserver`

API будет доступен по адресу:   
http://127.0.0.1:8000/api/.  
Используйте для входа:
- Логин: `admin`
- Пароль: `test`

## Основные эндпоинты API
* `/api/tests/`
* * `GET`: Получение списка всех тестов.
* * `POST`: Добавление нового генетического теста.
* `/api/tests?species=<вид>`
* * `GET`: Фильтрация тестов по виду (например, species=корова).
* `/api/statistics/`
* * `GET`: Получение агрегированной статистики.

## Лицензия
Этот проект распространяется под лицензией, указанной в корневом файле LICENSE.
