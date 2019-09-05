from aiohttp import web

from apps.rest import get_latest_price


async def server():
    app = web.Application()
    app.add_routes([web.get("/latest_price", get_latest_price)])
    return app
