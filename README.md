# CRUD для юзеров с токен аутентификацией

## Регистрация пользователя

POST http://127.0.0.1:8000/auth/users/ 

Parameters:
* username
* password
* email

Responses:
* User

## Аутентификация пользователя

POST http://127.0.0.1:8000/auth/token/login 

Parameters:
* username
* password

Responses:
* Token

## Получение задач пользователем 

GET http://127.0.0.1:8000/api/v1/task/

Headers:
* Authorization : Token {token}

Responses:
* Task

## Добавление задачи пользователем 

POST http://127.0.0.1:8000/api/v1/task/

Headers:
* Authorization : Token {token}

Parameters:
* title
* description

Responses:
* Task

## Редактирование задачи пользователем 

PUT http://127.0.0.1:8000/api/v1/task/{id}/

Headers:
* Authorization : Token {token}

Parameters:
* title
* description

Responses:
* Task

## Удаление задачи пользователем 

DELETE http://127.0.0.1:8000/api/v1/task/{id}/

Headers:
* Authorization : Token {token}
