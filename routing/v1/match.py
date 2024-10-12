from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
import uuid

from models.match import Match
from models.user import User
from schemas.match import MatchSchema, MatchListOpts
from services.auth import authenticated
from services.match import MatchService

router = APIRouter(prefix="/api/v1/match", tags=["match"])


@router.get(
    "",
    response_model=List[MatchSchema],
)
async def list(
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
    from_date: datetime | None = None,
    match_service: MatchService = Depends(),
    _: User = Depends(authenticated),
):
    matches = await match_service.list(MatchListOpts(
    limit=limit, offset=offset, from_date=from_date))
    return matches


@router.get(
    "/{match_id}",
    response_model=MatchSchema,
)
async def get(
    id: uuid.UUID,
    match_service: MatchService = Depends(),
    _: User = Depends(authenticated),
):
    match = await match_service.get(id)
    if not match:
        raise HTTPException(status_code=404, detail="MatchResponse not found")
    return match


@router.post(
    "",
    response_model=MatchSchema,
)
async def create(
    req: MatchSchema,  # Assuming MatchResponse Pydantic model is defined
    match_service: MatchService = Depends(),
    _: User = Depends(authenticated),
):
    match = await match_service.create(
        Match(
            id=req.id,
            opponent_team=req.opponent_team,
            date=req.date,
            result=req.result,
            stadium=req.stadium,
        )
    )
    return match


@router.delete(
    "/{id}",
    responses={200: {"msg": "successfully deleted"}},
)
async def delete(
    id: uuid.UUID,
    match_service: MatchService = Depends(),
    _: User = Depends(authenticated),
):
    await match_service.delete(id)
    return {"msg": "successfully deleted"}
