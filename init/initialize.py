
import asyncio
import datetime
from database.database import session_manager
from database.repositories.good_repository import GoodRepository

catalog = [
    {
        "name": "Настенный конвекционный газовый котел Baxi",
        "img": "/img/good-0.jpg",
        "price": 55080.,
        "sale": 0.,
        "stock": 12
    },
    {
        "name": "Газовая горелка Elco Vectron VG 1.40 E (одноступенчатая)",
        "img": "/img/good-1.png",
        "price": 217383.,
        "sale": 0.,
        "stock": 5
    },
    {
        "name": "Адаптер STOUT 90° DN60/100 м/п конденсационный с фланцем (совместим с Bosch) PP-AL",
        "img": "/img/good-2.jpg",
        "price": 4561,
        "sale": 0,
        "stock": 120
    },
    {
        "name": "Насосно-смесительный узел HOOBS коллектора теплого пола",
        "img": "/img/good-3.jpg",
        "price": 20208,
        "sale": 0,
        "stock": 12
    },
    {
        "name": "Напольный дизельный котел Navien LST-40KG",
        "img": "/img/good-4.jpg",
        "price": 106737,
        "sale": 0,
        "stock": 4
    },
    {
        "name": "Теплоноситель Warme Hydro 20 л",
        "img": "/img/good-5.jpg",
        "price": 779,
        "sale": 0,
        "stock": 102
    },
    {
        "name": "Аккумуляторная батарея Teplocom 100Ач герметичный свинцово-кислотный",
        "img": "/img/good-6.jpg",
        "price": 31190,
        "sale": 0,
        "stock": 56
    },
    {
        "name": "Meibes Victaulic Комплект переходников под сварку (2 шт.) ДУ 80",
        "img": "/img/good-7.jpg",
        "price": 7545,
        "sale": 0,
        "stock": 75
    }
]

async def main():
	async with session_manager.session() as session:
		goods = GoodRepository(session)
		for good in catalog:
			await goods.create(**good)#name=good['name'], img=good['img'], price=good['price'], sale=good['sale'], stock=good['stock'])
		await session.commit()


if __name__ == "__main__":
	asyncio.run(main())