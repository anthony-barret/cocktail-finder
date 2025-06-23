from fastapi import APIRouter

router = APIRouter()

@router.get("/ingredients")
async def list_ingredients():
    pass
