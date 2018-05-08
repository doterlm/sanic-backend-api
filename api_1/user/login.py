import asyncio
import asyncpg

import uvloop
from sanic import response

import api_1


# api_1=api_1.getbp()

@api_1.route('/a')
def a(request):
    return response.text('11')


@api_1.route('/b')
def b(request):
    return response.json({'b': 'b'}, 200)


@api_1.route('/c')
async def c(request):
    conn = await asyncpg.connect(host='locolhost', port=5432, user='postgres', password='postgres', database='sanicapi')
    await conn.execute('''
    CREATE TABLE a(id serial PRIMARY KEY,
                    name text)
                    ''')
    return response.text('22')
