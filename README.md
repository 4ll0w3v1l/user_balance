# User balance app

This app can create users, transfer amounts from user to user. This app stores data in-memory.

## How to run

~~~
docker build -t user-balance .
docker run -p 8000:8000 user-balance 
~~~

## How to test

open `127.0.0.1/docs` and test available methods