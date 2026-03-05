from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    pass


class DeploymentRow(Base):
    __tablename__ = 'deployment'
    id: Mapped[str] = Column(String, primary_key=True)
    db_name: Mapped[str] = Column(String)
    status: Mapped[str] = Column(String)
    username: Mapped[str] = Column(String)
    creation_time: Mapped[str] = Column(DateTime)