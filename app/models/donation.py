from sqlalchemy import Column, Text, ForeignKey, Integer

from app.core.db import Base
from .amount import Amount


class Donation(Amount, Base):
    comment = Column(Text)
    user_id = Column(Integer, ForeignKey('user.id'))
