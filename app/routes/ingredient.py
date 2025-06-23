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

# TODO: add ingredient
@router.post("/ingredient")
async def add_ingredient():
    pass

# TODO: update ingredient
@router.put("/ingredient/{ingredient_id}")
async def update_ingredient(ingredient_id):
    pass

# TODO: delete ingredient
@router.delete("/ingredient/{ingredient_id}")
async def delete_ingredient(ingredient_id):
    pass
