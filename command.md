# Commands

-https://www.markdownguide.org/basic-syntax/#:~:text=Headings,e.g.%2C%20%23%23%23%20My%20Header%20.

1. **python3 -m venv env** : _to create a virtual environment_
2. **source env/bin/activate** : _to activate the virtual environment_
3. **pip install django** : _to install Django_
4. **django-admin startproject project .** : _To create project in the parent folder_
5. **python manage.py (./manage.py) runserver** : _Will run the server_
6. **from django.core.management.utils import get_random_secret_key** : _To be executed in the python shell to enable generating secret key_
7. **print(get_random_secret_key())** : \*To print the secret key
8. **type python or python manage.py shell to prompt the interactive shell and Ctrl + K to quit from the python shell**
9. **pip freeze > requirements.txt** : _to log the packages on the project_
10. **pip install -r requirements.txt** : _To install all packages in the txt file_

# Packages Installed

django
python-dotenv 0.21.0
djangorestframework==3.14.0
pytest==7.2.0
