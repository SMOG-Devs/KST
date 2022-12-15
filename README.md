# KST - Kraków smog tracker

## Table of contents

> ### 1. [Project Description](#project-description)

> ### 2. [Setup](#setup)

## Project description

```
# TODO
```

## Setup

### BACKEND

#### 1. Install python 3.10 and Docker

#### 2. Create virtual environment

```bash
cd backend
# create virtual environment
python -m venv ./venv
# activate venv
# LINUX:
source venv/bin/activate
# WINDOWS:
./venv/Scripts/activate
# if you encounter "running scripts is disabled on this system" use this command and then ./venv/...
Set-ExecutionPolicy -Scope "CurrentUser" -ExecutionPolicy "RemoteSigned"

# install all requirements
pip install -r requirements.txt
```

#### 3. Create docker container with MySQL database.

1. Run the Docker
2. Start the container

```bash
# from backend directory
docker-compose -p kst-mysql-db -f docker-compose.yml up -d
```

To run the app you need to create `kst_db` database inside the MySQL container:

```bash
# open terminal inside the container
docker exec -it kst-mysql-db bash
# enter the MySQL console
mysql -u root -p
[ENTER PASSWORD](see `MySQL local db config` below)
```

Now enter following SQL queries:

```sql
-- create database
CREATE
DATABASE kst_db;
-- Check if db created successfully
SHOW
DATABASES;
```

Database is set up. You can run the app now

#### 4. Run the app:

````bash
cd backend
python run.py
````

#### 5. When you're done stop the app and container

```bash
docker-compose -p kst-mysql-db -f docker-compose.yml stop
# WARNING! If you run `docker-compose ... down` it will remove all images, networks, volumes etc.
# For data persistence use `stop`.
```

#### MySQL local db config:

```bash
username:   root
password:   secret_password
```

### FRONTEND

#### 1. Install Node.js and npm

```bash
# UNIX: 
sudo apt install nodejs
sudo apt install npm
# Windows:
# https://nodejs.org/en/download/
```

#### 2. Install React

```
npm install -g create-react-app  
```

#### 3. Run the frontend

```bash
npm start
```

[//]: # (# DB SETUP - tests)

[//]: # ()

[//]: # (```sql)

[//]: # ()

[//]: # (CREATE DATABASE kst_db;)

[//]: # ()

[//]: # (USE kst_db;)

[//]: # ()

[//]: # ()

[//]: # (-- create test table )

[//]: # ()

[//]: # (CREATE TABLE People &#40;)

[//]: # ()

[//]: # (    PersonID int,)

[//]: # ()

[//]: # (    FirstName varchar&#40;255&#41;,)

[//]: # ()

[//]: # (    LastName varchar&#40;255&#41;,)

[//]: # ()

[//]: # (    Address varchar&#40;255&#41;,)

[//]: # ()

[//]: # (    City varchar&#40;255&#41;)

[//]: # ()

[//]: # (&#41;;)

[//]: # ()

[//]: # ()

[//]: # (-- insert sample data )

[//]: # ()

[//]: # (INSERT INTO People VALUES )

[//]: # ()

[//]: # (                       &#40;1, "John", "Doe", "213 Warsaw", "Warsaw"&#41;;)

[//]: # ()

[//]: # (```)

[//]: # ()

[//]: # ()

[//]: # (# CREATE TABLES FROM app.py)

[//]: # ()

[//]: # (```python)

[//]: # ()

[//]: # (cd backend)

[//]: # ()

[//]: # (python)

[//]: # ()

[//]: # (from app import app, db)

[//]: # ()

[//]: # (with app.app_context&#40;&#41;:)

[//]: # ()

[//]: # (    db.create_all&#40;&#41;)

[//]: # ()

[//]: # (# now all tables created in the app.py will be created in the database as tables)

[//]: # ()

[//]: # (```)

[//]: # ()

[//]: # ()

[//]: # ()

[//]: # ()

[//]: # (## POWERSHELL ACTIVATE VENV:)

[//]: # ()

[//]: # (```)

[//]: # ()

[//]: # (cd backend)

[//]: # ()

[//]: # (Set-ExecutionPolicy Unrestricted -Scope Process  )

[//]: # ()

[//]: # (./venv/Scripts/activate)

[//]: # ()

[//]: # (```)
