from http.server import HTTPServer
from remotecontrol import RemoteControlHander

class TestHandler(RemoteControlHander):
    """testing handler"""

    keystring = 'ab:cd'

    def set_urls(self):
        self.urls = [
            ('^/noget/andet/$', self.itester),
        ]
    def itester(self):
        print('running insidetester')
        print(dir(self))

def run(server_class=HTTPServer, handler_class=TestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
