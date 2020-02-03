from fastapi import FastAPI
from .routers import users

# API Version Prefix URL for version 1 endpoints
# Probably not the right way to do this, just stub it for later
AVP1 = '/api/v1'

app = FastAPI(
        title = 'Fast API Try-Out',
        description = 'A first experiment creating an API with Python\'s FastAPI package.',
        version = '1.0.0',
)

app.include_router(
        users.router,
        prefix=AVP1 + '/users',
        tags=['users'],
)

@app.get('/')
async def root():
    return {'message': 'Hello World'}

@app.post('/{message}')
async def root(message: str = None):
    return message

@app.get('/files/{file_path:path}')
async def read_user_me(file_path: str = None):
    return {'file_path': file_path}
