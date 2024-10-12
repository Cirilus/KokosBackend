from typing import List, Type, Any

from fastapi import Depends

from models.match import Match
from repositories.match import MatchRepository
from schemas.match import MatchListOpts
from services.mixins.crud import CRUDServiceMixin


class MatchService(CRUDServiceMixin):
    def __init__(self, repo: MatchRepository = Depends()):
        super().__init__(repo)

    async def list(self, opts: MatchListOpts) -> List[Type[Match]]:
        return await self._repo.list(opts)