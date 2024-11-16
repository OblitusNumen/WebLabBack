#!/bin/bash

sudo docker run --name PostgreSQL -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres
sudo docker run --name Redis -p 6379:6379 -d redis
pip install sql alchemy
pip install sqlalchemy
pip install python-dotenv
pip install fastapi-controllers
pip install asyncpg alembic
pip freeze > requirements.txt
pip install redis
cd proxy
npm i http-proxy