# blessrng

Install all packages from requirements.txt:
- pip3 install -r requirements.txt

Update requirements with current installed packages:
- pip freeze > requirements.txt

# Migrations 
Create migration:
- python manage.py makemigrations app_name --name migration_name

Apply migrations:
- python manage.py migrate

# Database (PostgreSQL)
View all databases:
- \l

Select database:
- \c database_name

View all tables:
- \dt
