# Simple logging config that will output all logging.info() messages to stdout
# and right out these messages to "app.log" as well. Neat! :D

import logging

logging.basicConfig(
    format='%(asctime)s | %(levelname)s | %(message)s',
    filename='app.log',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S',
)
logging.getLogger().addHandler(logging.StreamHandler())

additional_data = {"Hello": "World!"}
logging.info("Here's my awesome message with additional data: %s", additional_data)


# Even better logging config to support utf-8 characters
logging.basicConfig(
    handlers=[
        logging.FileHandler('/log/file/path/app.log', 'a', 'utf-8'),
        logging.StreamHandler()
    ],
    format='%(asctime)s | %(pathname)s | %(levelname)s | %(message)s',
    level=logging.INFO
)

logging.info("Ответ пользователю: %s | текст: %s", chat_id, bot_response)
