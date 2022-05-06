# Getting Started
```shell
# Run Redis docker image
$ docker run -p 6379:6379 --name some-redis -d redis

# Check Redis running
$ docker exec -it some-redis redis-cli ping
```
- Create project directory, initialize git.
- Activate venv
- Install Django & create project
```shell
$ python3.9 -m venv env
$ source env/bin/activate

# Install Django & create project
(env)$ pip install django==3.2.9
(env)$ django-admin startproject django_celery_example .
(env)$ python manage.py startapp polls
```
- Add `requirements.txt` with celery, django, redis-py