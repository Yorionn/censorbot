# Telegram Censor Bot

Простой цензор-бот для Telegram, который удаляет сообщения определённого пользователя по ключевому слову.

## Настройка

1. Скопируйте `.env.example` в `.env` и заполните:
   - `BOT_TOKEN` - токен бота от @BotFather
   - `TARGET_USER_ID` - ID пользователя, сообщения которого нужно цензурить
   - `KEYWORD` - ключевое слово для поиска

2. Как узнать ID пользователя:
   - Добавьте бота @userinfobot в чат
   - Или используйте бота @getidsbot

## Запуск

### Локально

```bash
pip install -r requirements.txt
python bot.py
```

### Docker

```bash
docker build -t censorbot .
docker run --env-file .env censorbot
```

### Docker Compose

```yaml
version: '3.8'
services:
  bot:
    build: .
    env_file:
      - .env
    restart: unless-stopped
```

## Примечания

- Бот должен быть администратором чата с правами на удаление сообщений
- Ключевое слово ищется без учёта регистра
- Бот проверяет как текст сообщения, так и подпись к медиа


