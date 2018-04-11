from sanic import Blueprint
api_1=Blueprint('api_1',url_prefix='v1')
from .user import *