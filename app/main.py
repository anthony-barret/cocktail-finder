from fastapi import FastAPI

from app.db import engine
from app.models import Base
from app.routes import glassware, ingredient

app = FastAPI(title="Cocktail Finder API")

app.include_router(glassware.router, tags=["Glassware"])
app.include_router(ingredient.router, tags=["Ingredient"])

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
