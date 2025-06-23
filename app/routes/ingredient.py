from fastapi import APIRouter

router = APIRouter()

# TODO: list ingredients
@router.get("/ingredients")
async def list_ingredients():
    pass

# TODO: get ingredient
@router.get("/ingredient/{ingredient_id}")
async def get_ingredient(ingredient_id):
    pass

