# Заключительное задание первого модуля

Ваша задача в этом уроке — загрузить данные в Elasticsearch из PostgreSQL. Подробности задания в папке `etl`.

## Запуск проекта
1) cd 01_etl
2) cp .env.example .env
3) make build

## Описание сценариев Makefile
- `make build` - установить виртуальное окружение; установить необходимые зависимости для запуска контейнеров; добавить статические файлы; пересобрать контейнеры в интерактивном режиме
- `make buildd` -  установить виртуальное окружение; установить необходимые зависимости для запуска контейнеров; добавить статические файлы; пересобрать контейнеры в режиме демона
- `make run` - запустить контейнеры в интерактивном режиме
- `make rund` - запустить контейнеры в режиме демона 
- `make postman-test` - прогнать тесты апи  помощью сервиса Postman
- `make cli` - запустить консоль к контейнеру с бэкендом
- `make pre-commit` - установить виртуальное окружение; установить необходимые для запуска прекоммитов зависимости; добавить статические файлы; запустить выполнение инструкций прекоммита
- `make clean-pyc` - удалить все pyc-файлы из проекта
- `make clean-all` - остановить и удалить все контейнеры и занимаемую ими память и удалить все pyc-файлы из проекта
- `make clean` - остановить и удалить контейнеры соответствующие данному проекту и занимаемую ими память и удалить все pyc-файлы из проекта
