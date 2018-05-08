bind='127.0.0.1:8001'

backlog=2048
workers=2
worker_connections=100
worker_class='sanic.worker.GunicornWorker'
timeout=30
keepalive=2
# chdir='/root/sanicapi'

spew=False
daemon=False
umask=0