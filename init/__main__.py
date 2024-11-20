import asyncio

from database.database import session_manager
from database.repositories.good_repository import GoodRepository

catalog = [
    {
        "name": "Настенный конвекционный газовый котел Baxi",
        "img": "/img/good-0.png",
        "price": 55080.,
        "discount": 45.,
        "stock": 12
    },
    {
        "name": "Газовая горелка Elco Vectron VG 1.40 E (одноступенчатая)",
        "img": "/img/good-1.png",
        "price": 217383.,
        "discount": 30.,
        "stock": 5
    },
    {
        "name": "Адаптер STOUT 90° DN60/100 м/п конденсационный с фланцем (совместим с Bosch) PP-AL",
        "img": "/img/good-2.png",
        "price": 4561,
        "discount": 20.,
        "stock": 120
    },
    {
        "name": "Насосно-смесительный узел HOOBS коллектора теплого пола",
        "img": "/img/good-3.png",
        "price": 20208,
        "discount": 0.,
        "stock": 12
    },
    {
        "name": "Напольный дизельный котел Navien LST-40KG",
        "img": "/img/good-4.png",
        "price": 106737,
        "discount": 20.,
        "stock": 4
    },
    {
        "name": "Теплоноситель Warme Hydro 20 л",
        "img": "/img/good-5.png",
        "price": 779,
        "discount": 10.,
        "stock": 102
    },
    {
        "name": "Аккумуляторная батарея Teplocom 100Ач герметичный свинцово-кислотный",
        "img": "/img/good-6.png",
        "price": 31190,
        "discount": 5.,
        "stock": 56
    },
    {
        "name": "Meibes Victaulic Комплект переходников под сварку (2 шт.) ДУ 80",
        "img": "/img/good-7.png",
        "price": 7545,
        "discount": 70.,
        "stock": 75
    }
]


async def main():
    async with session_manager.session() as session:
        goods = GoodRepository(session)
        for good in catalog:
            await goods.create(
                **good)  # name=good['name'], img=good['img'], price=good['price'], discount=good['discount'], stock=good['stock'])
        await session.commit()


if __name__ == "__main__":
    asyncio.run(main())
