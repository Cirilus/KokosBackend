from typing import Sequence, Type, Any

from fastapi import Depends
from loguru import logger
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from configs.Database import get_db_connection
from models.match import Match
from repositories.mixins.crud import CRUDRepositoryMixin
from schemas.match import MatchListOpts


class MatchRepository(CRUDRepositoryMixin):
    def __init__(self, db: AsyncSession = Depends(get_db_connection)):
        super().__init__(Match, db)

    async def list(self, opts: MatchListOpts) -> Sequence[Type[Match]]:
        logger.debug(f"{self.model.__name__} - Repository - get_list")
        query = select(self.model).offset(opts.offset).limit(opts.limit)

        if opts.from_date is not None:
            query = query.where(Match.date >= opts.from_date)

        result = await self._db.execute(query)
        return result.scalars().all()