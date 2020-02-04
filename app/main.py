from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from .routers import users
import os
import json
from dotenv import load_dotenv
load_dotenv()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

# API Version Prefix URL for version 1 endpoints
# Probably not the right way to do this, just stub it for later
AVP1 = '/api/v1'

MYSQL_CREDENTIALS = json.loads(os.getenv('MYSQL_CREDENTIALS'))

app = FastAPI(
        title = 'Kaysh Cache API v1',
        description = 'A first experiment creating an API with Python\'s FastAPI package.',
        version = '1.0.0',
)

app.include_router(
        users.router,
        prefix=AVP1 + '/users',
        tags=['users'],
)


@app.get('/')
async def root(token: str = Depends(oauth2_scheme)):
    return {'message': 'Hello World', 'token': token}


@app.post('/{message}')
async def root(message: str = None):
    return message


@app.get('/files/{file_path:path}')
async def read_user_me(file_path: str = None):
    return {'file_path': file_path}

