from fastapi import APIRouter

router = APIRouter()

# TODO: list glassware
@router.get(path="/glasses")
async def list_glasses():
    pass
