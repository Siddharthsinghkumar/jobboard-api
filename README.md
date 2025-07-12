# JobBoard API

A backend REST API for managing job listings, built with **Django**, **PostgreSQL**, and **Redis**.  
Includes CRUD operations and a stats endpoint with caching support.

## 🚀 Features

- Create, view, update, and delete job listings (`/api/jobs/`)
- View total job count (`/api/stats/`) with Redis caching
- Built with Django REST Framework
- PostgreSQL database
- Redis cache integration

## 📦 Tech Stack

- Django 5.2.4
- Django REST Framework
- PostgreSQL
- Redis
- Docker (optional for deployment)

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jobboard-api.git
cd jobboard-api
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL

Create a PostgreSQL user and database:

```sql
CREATE DATABASE jobdb;
CREATE USER jobuser WITH PASSWORD 'jobpass';
ALTER ROLE jobuser SET client_encoding TO 'utf8';
ALTER ROLE jobuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE jobuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE jobdb TO jobuser;
GRANT ALL ON SCHEMA public TO jobuser;
ALTER SCHEMA public OWNER TO jobuser;
ALTER DATABASE jobdb OWNER TO jobuser;
```

Update `jobboard/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'jobdb',
        'USER': 'jobuser',
        'PASSWORD': 'jobpass',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Start Redis

```bash
sudo apt install redis-server
sudo systemctl enable redis
sudo systemctl start redis
```

### 6. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/api/jobs/` to see the API.

## 📬 API Endpoints

| Method | Endpoint       | Description             |
|--------|----------------|-------------------------|
| GET    | /api/jobs/     | List all jobs           |
| POST   | /api/jobs/     | Create a new job        |
| GET    | /api/jobs/<id> | Retrieve job details    |
| PUT    | /api/jobs/<id> | Update a job            |
| DELETE | /api/jobs/<id> | Delete a job            |
| GET    | /api/stats/    | Get total jobs count    |

## 📄 License

MIT License. Free for personal and educational use.