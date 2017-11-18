# Django Cheat Sheet

## Setting up Django locally (Mac)

#### Create a project directory and cd to it
```bash
mkdir projectname
```
```bash
cd projectname
```

#### Create a virtual environment named "myvenv" for your django project
```bash
python3 -m venv myvenv
```

#### Start virtual environment by running
```bash
source myvenv/bin/activate
```
If you are using PyCharm you will also need to set up myvenv there. Simply go to Preferences > Project > Project Interpreter and in the gear menu choose "Add local"

#### Make sure pip is up to date
```bash
pip install --upgrade pip
```

#### Install django module
This will install the latest version of Django:
```bash
pip install django
```
If you want to install a specific version of Django (for example django version 1.11.0):
```bash
pip install django~=1.11.0
```

#### Install Git (if haven't already)
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

#### Create Django project
While inside virtual environment myvenv (check if you see (myvenv) at the beginning of a terminal line) type:
```bash
django-admin startproject projectname .
```
Notice the . after the statement - it tells Django to install project files inside a current directory.



