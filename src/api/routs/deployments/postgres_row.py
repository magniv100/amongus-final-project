from sqlalchemy import Column, String, DateTime, engine, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    pass


engine = create_engine("postgresql://origa:password@localhost/postgres", echo=True)


class DeploymentRow(Base):
    __tablename__ = 'deployment'
    id: Mapped[str] = Column(String, primary_key=True)
    db_name: Mapped[str] = Column(String)
    status: Mapped[str] = Column(String)
    username: Mapped[str] = Column(String)
    creation_time: Mapped[str] = Column(DateTime)

Base.metadata.create_all(engine)