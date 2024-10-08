from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
import uuid
from models.news import News
from schemas.news import NewsCreateRequest, NewsResponse
from services.news import NewsService

router = APIRouter(prefix="/api/v1/news", tags=["news"])


@router.get(
    "",
    response_model=List[NewsResponse],
)
async def list(
    limit: Optional[int] = 100,
    offset: Optional[int] = 0,
    news_service: NewsService = Depends(),
):
    news_list = await news_service.list(limit, offset)
    return news_list


@router.get(
    "/{news_id}",
    response_model=NewsResponse,
)
async def get(id: uuid.UUID, news_service: NewsService = Depends()):
    news = await news_service.get(id)
    if not news:
        raise HTTPException(status_code=404, detail="News not found")
    return news


@router.post(
    "",
    response_model=NewsResponse,
)
async def create(
    req: NewsCreateRequest,  # Assuming News Pydantic model is defined
    news_service: NewsService = Depends(),
):
    news = await news_service.create(
        News(
            title=req.title,
            content=req.content,
        )
    )
    return news


@router.delete(
    "/{id}",
    responses={200: {"msg": "successfully deleted"}},
)
async def delete(id: uuid.UUID, news_service: NewsService = Depends()):
    await news_service.delete(id)
    return {"msg": "successfully deleted"}
