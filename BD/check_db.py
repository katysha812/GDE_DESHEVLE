
from db import Session
from models import Товары

session = Session()

try:
    товары = session.query(Товары).all()

    print("\nТовары приложения ГДЕДЕШЕВЛЕ")
    print("=" * 50)

    for товар in товары:
        print(
            f"Товар: {товар.название}\n"
            f"Цена: {товар.цена} руб.\n"
            f"Магазин: {товар.магазин.название}\n"
            f"Адрес: {товар.магазин.адрес}\n"
            f"Категория: {товар.категория.название}\n"
            + "-" * 50
        )

finally:
    session.close()
