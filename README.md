# Telegram Bot to transliterate cyrillic text
1. Установите Docker на свой компьютер, если вы еще этого не сделали. Вы можете найти инструкции по установке Docker на официальном сайте Docker.
2. Соберите Docker-образ с помощью команды docker build. Укажите путь к Dockerfile и имя образа. Например: `docker build -t mytelegrambot .`
3. После успешной сборки образа вы можете запустить контейнер с помощью команды docker run. Укажите имя образа и другие параметры, такие как проброс портов и переменные окружения. Например: `docker run -d -p 8080:8080 --name mybot <ID образа>`. Контейнер будет запущен в фоновом режиме (-d), порт 8080 будет проброшен на хостовую машину (-p 8080:8080), а контейнер будет назван mybot.
4. После запуска контейнера телеграмм бот будет доступен по указанному порту. Вы можете использовать этот порт для взаимодействия с ботом.
