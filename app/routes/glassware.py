from fastapi import APIRouter

router = APIRouter()

# TODO: list glassware
@router.get(path="/glasses")
async def list_glasses():
    pass

# TODO: add glassware
@router.post("/glass")
async def add_glass():
    pass

# TODO: delete glassware
@router.delete("/glass/{glass_id}")
async def delete_glass(glass_id):
    pass
