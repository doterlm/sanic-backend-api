import asyncio

import uvloop
from sanic import Sanic
from api_1.__init__ import api_1
app=Sanic(__name__)
app.blueprint(api_1,url_prefix='v1')
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
app.run(host='0.0.0.0',port=8000,debug=True)