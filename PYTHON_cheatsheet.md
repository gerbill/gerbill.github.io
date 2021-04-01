# Python Cheat Sheet #

Here I add some useful python code snippets.

#### Get current directory of a python script ####
```python
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
```

#### Upgrade pip in Windows venv
```bash
python -m pip uninstall pip setuptools
```
```bash
python -m pip install -U --force-reinstall pip
```
