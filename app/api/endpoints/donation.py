from typing import List
from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.schemas.donation import (
    DonationCreate, DonationDB, DonationLimitedDB
)
from app.models.user import User
from app.crud.donation import donation_crud
from app.services.investment import donation_investment

router = APIRouter()


@router.post(
    '/',
    response_model_exclude_none=True,
    response_model=DonationLimitedDB,
    dependencies=[Depends(current_user)],
)
async def create_donation(
        donation: DonationCreate,
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user),
):
    donation = await donation_crud.create(
        donation, session, user
    )
    await donation_investment(donation, session)
    return donation


@router.get(
    '/',
    response_model=List[DonationDB],
    response_model_exclude_none=True,
    dependencies=[Depends(current_superuser)],
)
async def get_all_donations(
    session: AsyncSession = Depends(get_async_session)
):
    """Только для суперюзеров."""
    donations = await donation_crud.get_multi(session)
    return donations


@router.get(
    '/my',
    response_model=List[DonationLimitedDB],
    response_model_exclude={'user_id'},
    dependencies=[Depends(current_user)],
)
async def get_my_reservations(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """Получает список всех пожертвований для текущего пользователя."""
    donations = await donation_crud.get_by_user(
        session=session, user=user
    )
    return donations
