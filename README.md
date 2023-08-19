# Запуск

Для запуска необходимы Docker и docker-compose.

```shell
docker-compose up --build
```

В файле `.env` находятся переменные окружения, которые используются в
контейнерах.

В папке `postman` находится Postman коллекция и переменные для неё. В самой
коллекции в папке `тесты` находится тестовый сценарий, в папке `api` описание
эндпоинтов.

# Описание API

## `GET /api/docs/`

Документация в формате ReDoc.

## `POST /api/auth/otp/`

Получение OTP для указанного номера телефона.

Входные данные
```json
{
    "phone_number": "+799999991"
}
```

Выходные данные
```json
{
    "phone_number": "+799999991",
    "otp": "5191"
}
```

## `POST /api/auth/verify/`

Аутентификация по номеру телефона и OTP.

Входные данные
```json
{
    "phone_number": "+799999991",
    "otp": "5191"
}
```

На выходе API передаёт куки `sessionid` и `csrftoken`.

## `GET /api/referrals/profile/`

Получение профиля текущего пользователя. Должны быть установлены куки
`sessionid` и `csrftoken`

Выходные данные
```json
{
    "phone_number": "+799999991",
    "invite_code": "2CPA3s",
    "referrals": [
    ]
}
```

Поле `referrer_code` не показывается, пока пользователь не активировал
инвайт-код.

## `PUT /api/referrals/profile/`

Установка инвайт-кода для текущего пользователя. Должны быть установлены куки
`sessionid` и `csrftoken`. HTTP заголовок `X-CSRFToken` должен быть равен
`csrftoken` для текущего `sessionid`.

Входные данные
```json
{
    "referrer_code": "5tsjV3"
}
```

Выходные данные
```json
{
    "phone_number": "+799999991",
    "invite_code": "2CPA3s",
    "referrer_code": "5tsjV3",
    "referrals": [
    ]
}
```
