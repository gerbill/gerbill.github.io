# Django Cheat Sheet

## Setting up Django locally (Mac)

### Create a project directory and cd to it
```bash
mkdir projectname
```
```bash
cd projectname
```

### Create a virtual environment named "myvenv" for your django project
```bash
python3 -m venv myvenv
```

### Start virtual environment by running
```bash
source myvenv/bin/activate
```
If you are using PyCharm you will also need to set up myvenv there. Simply go to Preferences > Project > Project Interpreter and in the gear menu choose "Add local"

### Make sure pip is up to date
```bash
pip install --upgrade pip
```

### Install django module
This will install the latest version of Django:
```bash
pip install django
```
If you want to install a specific version of Django (for example django version 1.11.0):
```bash
pip install django~=1.11.0
```

### Install Git (if haven't already)
To install git for your system follow instructions on Git website: https://git-scm.com/. I also recommend creating a bitbucket account https://bitbucket.org/account/signup/ to create remote repositories there.

Now create a .gitignore file inside your project directory:
```bash
nano .gitignore
```
Once insede the nano editor type the following to exclude .idea, myvenv and __pycache__ from being added to git:
```bash
.idea/
myvenv/
__pycache__/
```
Now to save .gitignore file press Control+O and to exit nano editor press Control+X

### Create Django project
While inside virtual environment myvenv (check if you see (myvenv) at the beginning of a terminal line) type:
```bash
django-admin startproject projectname .
```
Notice the . after the statement - it tells Django to install project files inside a current directory.


## Integrate with Postgres
Assuming you've got PostgreSQL already running on your machine

### Prepare a database

Get into psql in terminal
```bash
psql
```

Create a new database my_project_database
```sql
CREATE DATABASE my_project_database;
```

Create a user for your new database
```sql
CREATE USER my_project_user WITH PASSWORD 'password';
```

Adjust user
```sql
ALTER ROLE my_project_user SET client_encoding TO 'utf8';
ALTER ROLE my_project_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE my_project_user SET timezone TO 'UTC';
```

Give my_project_user access to my_project_database
```sql
GRANT ALL PRIVILEGES ON DATABASE my_project_database TO my_project_user;
```

Exit psql
```sql
\q
```

### Install python postgres module
```bash
pip install psycopg2
```

### Configure django project settings to use PostgreSQL
Open settings.py in editor. Change this code
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```
To this code
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'my_project_database',
        'USER': 'my_project_user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### Migrate the Database and Test your Project

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### Create SuperUser for your django project

```bash
python manage.py createsuperuser
```
Then you'll be asked a set of questions. Use strong password when asked for a password

### Run a development server to test your project
```bash
python manage.py runserver 0.0.0.0:8000
```
Once your project is reachable through browser at http://localhost:8000 try going to http://localhost:8000/admin to see if django admin area works. You shojld be able to log in using credentials you set when you were creating a superuser.
