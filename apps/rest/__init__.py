from aiohttp import web

from apps.connections import RedisConnection


async def get_latest_price(request):
    latest_price = await MarketValueFetcher().get_latest_price()
    return web.json_response(latest_price, status=200)


class MarketValueFetcher:
    """
    Class for fetching the latest market values from cache
    """

    proj = "rest_fetcher"

    def __init__(self, crypto="BTC", currency="USD"):
        self.crypto = crypto
        self.currency = currency

    async def get_latest_price(self):
        cache_key = f"{self.crypto}:{self.currency}:ticker:current_price"
        async with RedisConnection() as aredis:
            value = await aredis.hget(key=cache_key, field="latest_price")
            return float(value.decode("utf-8"))
