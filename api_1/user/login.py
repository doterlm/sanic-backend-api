from sanic import response

from api_1._init_ import api_1


@api_1.route('/a')
def a(request):
    return response.text('11')