import redis
from fastapi import Depends
from fastapi_controllers import Controller, get, post
from sqlalchemy.ext.asyncio import AsyncSession

from back.authorize_user import authorize_user
from back.schemas.catalog import Cart
from database.database import get_db_session
from database.models.user import User
from database.redis import RedisDB, get_redis_client
from database.repositories.good_repository import GoodRepository


class CatalogController(Controller):
    prefix = '/catalog'
    tags = ['catalog']

    def __init__(self, session: AsyncSession = Depends(get_db_session)):
        self.session = session

    @get("/", summary="returns all goods in repository", description="Get all goods")
    async def get_goods(self):
        goods = await GoodRepository(self.session).get_all()
        return list([{"id": good.id, "label": good.name, "price": good.price, "discount": good.discount,
                      "path_to_image": good.img, "in_stock": good.stock} for good in goods])

    @get("/cart", summary="returns cart for authorized user", description="Get user's cart")
    async def get_cart(self, redis: redis.Redis = Depends(get_redis_client), user: User = Depends(authorize_user)):
        print("a")
        cart = redis.get(f"{RedisDB.cart}:{user.id}")
        print("b")
        if cart is None:
            return Cart(contents=[], discount=False)
        return await self.normalize_cart(Cart.model_validate_json(cart.decode('utf-8')))

    @post("/updcart", summary="validates and updates cart for authorized user", description="Update cart")
    async def update_cart(self, cart: Cart, redis: redis.Redis = Depends(get_redis_client),
                          user: User = Depends(authorize_user)):
        await self.normalize_cart(cart)
        redis.set(f"{RedisDB.cart}:{user.id}", cart.model_dump_json())
        return {"message": "OK"}

    @get("/getitem", summary="returns good with specified id", description="Get good by id")
    async def getGood(self, id: uuid.UUID):
        good = await GoodRepository(self.session).get_by_id(id)
        return good

    async def normalize_cart(self, cart: Cart) -> Cart:
        goods = await GoodRepository(self.session).get_all()
        for item in cart.contents:
            for good in goods:
                if item.id == good.id and item.count > good.stock:
                    item.count = good.stock
        return cart
