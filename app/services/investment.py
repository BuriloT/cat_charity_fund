from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models import CharityProject, Donation
from app.schemas.charity_project import CharityProjectDB
from app.schemas.donation import DonationDB


async def investment(
    project,
    donation,
    session: AsyncSession
):
    donat_remainder = donation.full_amount - donation.invested_amount
    project_remainder = project.full_amount - project.invested_amount
    if project_remainder <= donat_remainder:
        donation.invested_amount += project_remainder
        setattr(project, 'invested_amount', project.full_amount)
        setattr(project, 'close_date', datetime.now())
        setattr(project, 'fully_invested', True)
        if project_remainder == donat_remainder:
            setattr(donation, 'close_date', datetime.now())
            setattr(donation, 'fully_invested', True)
    if project_remainder > donat_remainder:
        project.invested_amount += donat_remainder
        setattr(donation, 'invested_amount', donation.full_amount)
        setattr(donation, 'close_date', datetime.now())
        setattr(donation, 'fully_invested', True)


async def project_investment(
    project: CharityProjectDB,
    session: AsyncSession
):
    donations = await session.execute(
        select(Donation).where(
            Donation.fully_invested == False # noqa
        )
    )
    donations = donations.scalars().all()
    for donation in donations:
        await investment(project, donation, session)
    await session.commit()
    await session.refresh(project)


async def donation_investment(
    donation: DonationDB,
    session: AsyncSession
):
    projects = await session.execute(
        select(CharityProject).where(
            CharityProject.fully_invested == False # noqa
        )
    )
    projects = projects.scalars().all()
    for project in projects:
        await investment(project, donation, session)
    await session.commit()
    await session.refresh(donation)
