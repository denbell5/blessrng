Create virtual environment (has to be created in folder 'env' on the same level where manage.py is to be ignored by git)
```
python3 -m venv env
```

Activate virtual environment:
```
& ./env/Scripts/Activate.ps1
```

Create superuser:
```
python manage.py createsuperuser
```

Install all packages from requirements.txt:
```
pip3 install -r requirements.txt
```


Update requirements with current installed packages:
```
pip freeze > requirements.txt
```


## Migrations 
Create migration:
```
python manage.py makemigrations app_name --name migration_name
```


Apply migrations:
```
python manage.py migrate
```


## Database (PostgreSQL)
View all databases:
```
\l
```


Select database:
```
\c database_name
```


View all tables:
```
\dt
```
