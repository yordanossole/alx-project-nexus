# Social Media API (Django REST)

Backend for a social platform built with Django REST Framework, PostgreSQL, JWT auth, and Swagger docs. Provides posts, users, stories, chat, and feed APIs with pagination and filtering.

## Tech Stack
- Django 5, Django REST Framework
- PostgreSQL, Redis (Channels configured)
- JWT (djangorestframework-simplejwt)
- Swagger/Redoc (drf-yasg)
- django-filter for query filtering

## Quick Start

### Run with Docker (recommended)
```bash
docker compose up --build
```
- API: http://localhost:8010/
- Swagger: http://localhost:8010/swagger/
- Redoc: http://localhost:8010/redoc/

The compose file provisions Postgres and Redis, runs migrations and collects static, then starts the server.

### Run locally
Requirements: Python 3.10+, PostgreSQL, Redis

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

export DB_NAME=your_db
export DB_USER=your_user
export DB_PASSWORD=your_password
export DB_HOST=localhost
export DB_PORT=5432

python src/manage.py makemigrations
python src/manage.py migrate
python src/manage.py createsuperuser
python src/manage.py runserver 0.0.0.0:8010
```

Notes:
- Settings module: `config.settings`
- `APPEND_SLASH=False` → endpoints require trailing slashes (e.g., `/user/me/`).

## Authentication
JWT via `djangorestframework-simplejwt`.
- Login: `POST /auth/login/` → returns access/refresh
- Auth header: `Authorization: Bearer <access>`
- Logout (blacklist refresh): `POST /auth/logout/`
- Change password: `POST /auth/change-password/`

## API Documentation
- Swagger UI: `/swagger/`
- Redoc: `/redoc/`
- Root `/` redirects to `/swagger/`

## Apps and Endpoints

### Users (`/user/` and `/users/`)
- `GET /user/me/`
- `GET /user/{username}/`
- `POST /user/{username}/follow/`
- `POST /user/{username}/unfollow/`

### Auth (`/auth/`)
- `POST /auth/register/`
- `POST /auth/login/`
- `POST /auth/logout/`
- `POST /auth/change-password/`

### Posts (`/posts/`)
- `GET /posts/` (paginated)
- `POST /posts/`
- `GET|PUT|PATCH|DELETE /posts/{id}/`
- `POST /posts/{id}/comments/`
- `POST|DELETE /posts/{id}/like/`

### Stories (`/stories/`)
- `GET /stories/`
- `POST /stories/`
- `POST /stories/viewed/`

### Chat (`/chats/`)
- `GET|POST /chats/rooms/` (filterable by `name`)
- `GET /chats/rooms/{room_id}/messages/` (filterable by `sender`)
- `POST /chats/rooms/{room_id}/messages/new/`

### Feed (`/feed/`)
- `GET /feed/` (filterable by `user`, `post`)

## Pagination and Filtering
- Pagination: page-number pagination via `config.pagination.DefaultPagination`
  - Query params: `?page=1&page_size=20`
- Filtering: `django-filter` on supported list endpoints

## Environment Variables
These can be set via your shell or docker compose:
- `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`
- `REDIS_HOST`, `REDIS_PORT`
- `DEBUG` (default `True` for local)

## Static and Media
- Static collected to `src/staticfiles/` (compose runs `collectstatic`)
- Media uploads stored under app-specific upload paths (e.g., `post_images/`, `stories/`)

## Admin
- `/admin/` (create a superuser to access)

## Development Notes
- Custom user model: `users.User` (email is `USERNAME_FIELD`)
- Ensure requests use trailing slashes (`APPEND_SLASH=False`)
- Global default permissions require auth; Swagger auth supported

## Troubleshooting
- 404 on endpoints: confirm trailing slash and correct base route (e.g., `/posts/`, not `/posts`)
- DB connection errors: verify Postgres env vars and service availability
- Swagger not loading: ensure `drf-yasg` installed and server running on port 8010
