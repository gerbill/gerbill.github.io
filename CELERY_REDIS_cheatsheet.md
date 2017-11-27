# CELERY and REDIS CHEAT SHEET

## Redis
### Redis Installation
#### Install Redis on Ubuntu
```bash
sudo apt-get update
```
```bash
sudo apt-get upgrade
```
```bash
sudo apt install redis-server
```
#### Install Python-Redis
Always best to use virtualenv (here your virtual envirnomnet gonna be named "env"):
```bash
python3 -m venv env
```
Activate virtualev "env":
```bash
source env/bin/activate
```
While inside virtualenv "env" install python-redis:
```bash
pip install redis
```

### Using Redis in Python
```python
import redis

# Create a connection to redis database
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0)

# Store key-value pair
redis_db.set("my_key", "my_value")

# Retrieve my_value by my_key
my_value = redis_db.get("my_key")

# Get all keys from the redis_db
all_keys = redis_db.keys()

# Delete all keys from the redis_db
redis_db.flushdb()
```
More info on redis commands: [http://redis-py.readthedocs.io/en/latest/](http://redis-py.readthedocs.io/en/latest/)
