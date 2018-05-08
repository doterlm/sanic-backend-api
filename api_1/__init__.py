from sanic import Blueprint
api_1 = Blueprint('api_1')


def getbp():
    return api_1

from .qiniu import qiniuapi
from .user import login