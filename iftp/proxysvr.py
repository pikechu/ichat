# 代理服务
# 1. 包头校验
# 2. 调用服务发现, 创建连接
# 3. 转发
import socketserver

from gevent import monkey
monkey.patch_all()
import socket

class Server(socketserver.TCPServer):
    def __init__(self):
        pass

    def run(self):
        socketserver.TCPServer


class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):





