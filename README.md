Коллекция содержит все 4 сценария с mock ответами.
Python автотесты реализованы через unittest с mock API-ответами. Не забудьте поставить requests-mock.
Для реального выполнения тестов нужны были API-токен Qiwi, PERSON_ID и тестовый номер телефона...

Для скрипта использовал Python unittest, а не Playwright, для REST API проще использовать HTTP-клиент.

Инструкция по запуску коллекции с Mock Server:

Импортировать коллекцию
Создать Mock Server
Postman выдаст URL мок-сервера
В коллекции открыть раздел Variables
Установить base_URL = выданный Mock Server URL
