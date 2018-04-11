from sanic import response
from run import app


@app.route('/a')
def a(request):
    return response.text('11')