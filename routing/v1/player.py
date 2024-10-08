from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
import uuid
from models.palyer import Player
from schemas.palyer import PlayerSchema
from services.palyer import PlayerService

router = APIRouter(prefix="/api/v1/player", tags=["player"])


@router.get(
    "",
    response_model=List[PlayerSchema],
)
async def list(
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
    player_service: PlayerService = Depends(),
):
    players = await player_service.list(limit, offset)
    return players


@router.get(
    "/{player_id}",
    response_model=PlayerSchema,
)
async def get(id: uuid.UUID, player_service: PlayerService = Depends()):
    player = await player_service.get(id)
    if not player:
        raise HTTPException(status_code=404, detail="PlayerSchema not found")
    return player


@router.post(
    "",
    response_model=PlayerSchema,
)
async def create(req: PlayerSchema, player_service: PlayerService = Depends()):
    player = await player_service.create(
        Player(
            id=req.id,
            firstname=req.firstname,
            middelname=req.middelname,
            lastname=req.lastname,
            played_from=req.played_from,
            biography=req.biography,
            position=req.position,
            achievements=req.achievements,
        )
    )
    return player


@router.delete(
    "/{id}",
    responses={200: {"msg": "successfully deleted"}},
)
async def delete(id: uuid.UUID, player_service: PlayerService = Depends()):
    await player_service.delete(id)
    return {"msg": "successfully deleted"}
