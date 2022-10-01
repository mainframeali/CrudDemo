# handle API routing
from fastapi import APIRouter
from endpoint import crud

router = APIRouter()
router.include_router(crud.router)
