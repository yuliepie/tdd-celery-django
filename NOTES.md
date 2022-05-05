# Getting Started
```shell
# Run Redis docker image
$ docker run -p 6379:6379 --name some-redis -d redis

# Check Redis running
$ docker exec -it some-redis redis-cli ping
```
- Create project directory, initialize git.
- Activate venv
```shell
$ python3.9 -m venv env
$ source env/bin/activate
```