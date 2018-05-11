from sanic import response

from api_1.__init__  import api_1
from qiniu import Auth


access_key='KyyJ2b9IhoNBKtRNLaKphZ0SfNxI0g9pKedgGNPo'
secret_key='HXQ8JNTnwoYeRb1AMDctYpEzhdKZzF9LOPiv-A2U'
q=Auth(access_key,secret_key)
bucket_domain='p8aitf97j.bkt.clouddn.com'


# 获取七牛资源链接
@api_1.route('/qiniudown/<tag1>')
async def qiniudown(request,tag1):
    filename = tag1+'.MP3'
    base_url = 'http://%s/%s' % (bucket_domain, filename)
    private_url=q.private_download_url(base_url,expires=3600)
    return response.json({'url': format(private_url)}, 200)

# 上传歌曲
# @api_1.route('/qiniuup/<>')


