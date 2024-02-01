## 💾 File Server API

👉 Тестовое задание: Загрузка и обработка файлов
```
Цель:
Разработать Django REST API, который позволяет загружать файлы на сервер,
а затем асинхронно обрабатывать их с использованием Celery.
Требования:
Использовать Django REST Framework для создания API.
Создать API эндпоинт upload/, который будет принимать POST-запросы для загрузки файлов.
При загрузке файла необходимо создать объект модели File,
сохранить файл на сервере и запустить асинхронную задачу для обработки файла с использованием Celery.
В ответ на успешную загрузку файла вернуть статус 201 и сериализованные данные файла.
Реализовать Celery задачу для обработки файла.
Задача должна быть запущена асинхронно и изменять поле processed модели File на True после обработки файла.
Реализовать API эндпоинт files/, который будет возвращать список всех файлов с их данными, включая статус обработки.
```

## 🛠 Tests
```
Name                                         Stmts   Miss  Cover
----------------------------------------------------------------
backend/__init__.py                              2      0   100%
backend/celery.py                                6      0   100%
backend/settings.py                             35      0   100%
backend/urls.py                                  8      0   100%
config.py                                       10      0   100%
file_server_app/__init__.py                      0      0   100%
file_server_app/admin.py                         3      0   100%
file_server_app/apps.py                          6      0   100%
file_server_app/docs.py                          3      0   100%
file_server_app/migrations/0001_initial.py       7      0   100%
file_server_app/migrations/__init__.py           0      0   100%
file_server_app/models.py                       16      0   100%
file_server_app/serializers.py                  10      0   100%
file_server_app/signals.py                       8      0   100%
file_server_app/tasks.py                         7      0   100%
file_server_app/tests.py                        39      0   100%
file_server_app/urls.py                          7      0   100%
file_server_app/utils.py                        22      0   100%
file_server_app/validators.py                    9      0   100%
file_server_app/views.py                        20      0   100%
manage.py                                       12      2    83%
----------------------------------------------------------------
TOTAL                                          230      2    99%

```






