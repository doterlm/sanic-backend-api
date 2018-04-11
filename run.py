from sanic import Sanic
from api_1._init_ import api_1
app=Sanic(__name__)
app.blueprint(api_1,url_prefix='v1')
# app.run(host='0.0.0.0',port=8000,debug=True)