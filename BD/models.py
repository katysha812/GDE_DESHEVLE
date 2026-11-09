
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    ForeignKey,
    DateTime,
    Boolean
)

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

SCHEMA = "gde_deshevle"


# -------------------------
# Таблица магазинов
# -------------------------

class Магазины(Base):
    __tablename__ = "магазины"
    __table_args__ = {"schema": SCHEMA}

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    название = Column(String(255), nullable=False)
    адрес = Column(String(500), nullable=False)
    город = Column(String(100), nullable=False)
    телефон = Column(String(20))
    активен = Column(Boolean, default=True)

    товары = relationship(
        "Товары",
        back_populates="магазин"
    )


# -------------------------
# Таблица категорий
# -------------------------

class Категории(Base):
    __tablename__ = "категории"
    __table_args__ = {"schema": SCHEMA}

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    название = Column(String(255), nullable=False, unique=True)

    товары = relationship(
        "Товары",
        back_populates="категория"
    )


# -------------------------
# Таблица товаров
# -------------------------

class Товары(Base):
    __tablename__ = "товары"
    __table_args__ = {"schema": SCHEMA}

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    название = Column(String(255), nullable=False)

    описание = Column(String(500))

    цена = Column(Float, nullable=False)

    единица_измерения = Column(String(50), default="шт.")

    дата_обновления = Column(
        DateTime,
        server_default=func.now()
    )

    id_магазина = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.магазины.id"),
        nullable=False
    )

    id_категории = Column(
        Integer,
        ForeignKey(f"{SCHEMA}.категории.id"),
        nullable=False
    )

    магазин = relationship(
        "Магазины",
        back_populates="товары"
    )

    категория = relationship(
        "Категории",
        back_populates="товары"
    )
