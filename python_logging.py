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
