import asyncpg

from sanic import response

from api_1.__init__  import api_1
from qiniu.services.cdn.manager import create_timestamp_anti_leech_url
import time

#
#
# # @api_1.route('/qiniu')
# host='http://p8aitf97j.bkt.clouddn.com'
# encrypt_key=''
filename = '一生所爱_纯音频文件_纯音频输出.MP3'
# query_string=''
#
# deadline=int(time.time())+3600
# timestamp_url=create_timestamp_anti_leech_url(host,filename,query_string,encrypt_key,deadline)
# print(timestamp_url)
import requests
from qiniu import Auth


# access_key='KyyJ2b9IhoNBKtRNLaKphZ0SfNxI0g9pKedgGNPo'
# secret_key='HXQ8JNTnwoYeRb1AMDctYpEzhdKZzF9LOPiv-A2U'
# q=Auth(access_key,secret_key)
# bucket_domain='p8aitf97j.bkt.clouddn.com'
# base_url='http://%s/%s'%(bucket_domain,filename)
# private_url=q.private_download_url(base_url,expires=3600)
# print(private_url)
#
# r=requests.get(private_url)
# assert r.status_code==200

@api_1.route('/qiniudown/<tag1>/<tag2>')
async def qiniudown(request,tag1,tag2):
    print(request)

    return response.json({'a': format(tag1),'b': format(tag2)}, 200)
