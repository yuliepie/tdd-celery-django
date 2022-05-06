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
- Add `requirements.txt` with celery, django, redis-py & install
- Set up Celery & broker with Celery config

# Running Celery
- Run Celery: `(env)$ celery -A django_celery_example worker --loglevel=info`
- This spins up Celery task queue and workers, using the broker URL (In a separate celery terminal)
- Apply inital migrations: `python manage.py migrate`

## Send Celery task from Django shell
```shell
# Enter Django shell
(env)$ python manage.py shell

# Import Celery task
>>> from django_celery_example.celery import divide
>>> task = divide.delay(1, 2) # Command to push a Celery task
```
- use `delay` method to send message to broker. A celery worker then picks up and executes the `divide` task.
- Check Celery terminal - Can see the task was received, and succeeded after 5 seconds.
- Basic Flow:
  - Celery client (producer) -> add task to queue via broker
  - Celery worker (consumer) -> gets task from queue via broker
  - When task is complete, results are stored in the Result backend
- `task` variable object:
  - `type(task)` yields class `celery.result.AsyncResult`
  - Stores various information about the task
  - `task.state`: State of the task
  - `task.result`: Return value of task (will return Error in case of Exception)
  > `print(task.state, task.result)`

# Flower
- Real-time monitoring & admin tool for Celery
- Can easily visualize task status and quicker instant feedback than terminal
- Add flower to `requirements.txt` & install
- Spin up flower server: `(env)$ celery -A django_celery_example flower --port=5555`
- View flower dashboard at `http://localhost:5555`
- Add few tasks from django shell => Flower dashboard shows tasks with their state, ID, arguments, result, exceptions etc
- `UUID` column: `id` of `AsyncResult` task object. Can copy UUID of task and view details from Django shell
```shell
>>> from celery.result import AsyncResult
>>> task = AsyncResult('9c62f554-82a3-4718-b9b7-66f425328373')  # replace with your UUID
>>> task.state
'FAILURE'
>>> task.result
ZeroDivisionError('division by zero')
```