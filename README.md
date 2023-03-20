# reddit-feed-api

Reddit Feed API is a REST API that allows you to:
1. Get a list of posts from a reddit feed
2. Create a new post

## Setup Guide

A quick guide to setup auth service on your local machine

Clone the repository

```sh
$ git clone https://github.com/Ehbraheem/reddit-feed-api.git
$ cd reddit-feed-api
```

## Installation Guide

#### Setting up with Docker 🐳

Docker is a containerization platform, it allows you to run applications in a sandboxed environment. This means that you can run the application without having to install all the dependencies on your machine. This is especially useful if you are working on a project with multiple dependencies and you don't want to install them all on your machine.

You will need Docker installed on your machine. [Do it here in the Docker website](https://www.docker.com/products/docker-desktop).

After that you'll need to follow these steps:

### 1. Add local environment variables

**Note:** You can skip this step if you are using the `.env` file provided in the repository.

> This is important because the application needs those variables to run properly.

1. Create `.env` file in the root directory of the project (same level as `docker-compose.yml` file).
2. Add the following variables to the `.env` file:

```bash
PROJECT_NAME=reddit-feed-api
BACKEND_CORS_ORIGINS=["http://localhost:8000", "https://localhost:8000", "http://localhost", "https://localhost"]


POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_SERVER=database
POSTGRES_DB=app
POSTGRES_TEST_DB=app_test
```

### 2. Start the application

> This command starts the app and all its dependent services like database.

```bash
docker-compose up
```

You can access the app in your browser using [http://0.0.0.0:8000/](http://0.0.0.0:8000/)

Documentation for the API can be found at [http://0.0.0.0:8000/docs](http://0.0.0.0:8000/docs) and [http://0.0.0.0:8000/redoc](http://0.0.0.0:8000/redoc)

## Installation Guide

## Running the tests

You can run the tests using the following command:

```sh
docker-compose run app pytest
```

## License

This project is licensed under the terms of the MIT license.
