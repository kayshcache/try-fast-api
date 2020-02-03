from fastapi import APIRouter

router = APIRouter()

@router.get('/', tags=['users'])
async def read_users():
    return [{'username': 'First User'}]
