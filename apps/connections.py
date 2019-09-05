import aioredis

from config import Config


class RedisConnection:
    def __init__(self):
        self.url = f"redis://{Config.REDIS_HOST}"
        self.connection = None

    async def __aenter__(self):
        self.connection = await aioredis.create_redis(self.url)
        return self.connection

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
        await self.connection.wait_closed()
