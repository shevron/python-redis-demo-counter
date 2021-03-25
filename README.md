# Sample App: Python + FastAPI + Redis Counter

This tiny sample application is used to demonstrate talking to Redis from 
Python. It was written for educational purposes, and has no production 
use case. 

## Running

### Using Docker
The app is available as a Docker image:

    $ docker run --rm shevron/python-redis-demo-counter

You may need to set some environment variables (see below) to point to 
your Redis server.

### Using Docker-compose
You can run this app by pulling the code and then using Docker Compose. 

    $ docker-compose up --build

This will launch the app, listening on http://localhost:8000, as well
as a Redis server to be used as backend. 

## Configuration
Set the `REDIS_HOST` and `REDIS_PORT` environment variables to point to your
Redis server host and port, respectively. If not set, the app will default to
using `localhost:6379`

## Usage
This app holds multiple "counters", with each counter being available 
at `http://localhost:8000/<counter_name>` where `<counter_name>` can be 
any string of alphanumeric characters as well as dashes and underscores. 

Sending a `GET` request to the counter endpoint will return its value:

    $ curl http://localhost:8000/goats-eaten
    0

While sending a `POST` request to the counter endpoint will increase the
counter by 1, and return its current value:

    $ curl -X POST http://localhost:8000/goats-eaten
    1

    $ curl -X POST http://localhost:8000/goats-eaten
    2

## License
[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the author has waived all copyright and 
related or neighboring rights to this work.
