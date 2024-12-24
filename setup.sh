#!/bin/bash

sudo docker run --name PostgreSQL -p 5432:5432 -e POSTGRES_PASSWORD=1234 -d postgres
sudo docker run --name Redis -p 6379:6379 -d redis
pip3 install alembic
pip3 install annotated-types
pip3 install anyio
pip3 install asyncpg
pip3 install click
pip3 install fastapi
pip3 install fastapi-controllers
pip3 install greenlet
pip3 install h11
pip3 install httptools
pip3 install idna
pip3 install Mako
pip3 install MarkupSafe
pip3 install pydantic
pip3 install pydantic_core
pip3 install python-dotenv
pip3 install PyYAML
pip3 install redis
pip3 install sniffio
pip3 install SQLAlchemy
pip3 install starlette
pip3 install typing_extensions
pip3 install uvicorn
pip3 install uvloop
pip3 install watchfiles
pip3 install websockets
pip3 install Werkzeug
pip freeze > requirements.txt
pip install redis
cd proxy
npm i http-proxy