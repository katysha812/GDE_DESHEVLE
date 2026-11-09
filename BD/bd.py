from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base

# Подключение к новой базе данных gdedeshevle
DB_URI = (
    "postgresql+psycopg2://postgres:1234"
    "@localhost:5432/gdedeshevle"
)

engine = create_engine(DB_URI, echo=True)

try:
    with engine.connect() as connection:
        print("Успешное подключение к gdedeshevle!")

        connection.execute(
            text("CREATE SCHEMA IF NOT EXISTS gde_deshevle")
        )
        connection.commit()

except Exception as e:
    print(f"Ошибка подключения: {e}")
    raise

# Создаём таблицы из models.py
Base.metadata.create_all(engine)

# Создаём сессии
Session = sessionmaker(bind=engine)

print("Таблицы успешно созданы!")
