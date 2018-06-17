import re
import base64
from http.server import SimpleHTTPRequestHandler

class RemoteControlHander(SimpleHTTPRequestHandler):
    """Handles get requests to trigger remote control of the system"""

    urls = []
    keystring = ''

    def __init__(self, *args, **kwargs):
        self.set_urls()
        self.key = base64.b64encode(str.encode(self.keystring))
        super(RemoteControlHander, self).__init__(*args, **kwargs)

    def populate_urls(self):
        pass

    def do_HEAD(self, code=200):
        self.send_response(code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm=\"Remote control\"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        if self.headers.get('Authorization') == None:
            self.do_AUTHHEAD()
            pass
        elif self.headers.get('Authorization') == 'Basic ' + self.key.decode():
            mo = None
            for url in self.urls:
                mo = re.fullmatch(url[0], self.path)
                if mo:
                    self.do_HEAD()
                    try:
                        url[1]()
                    except Exception as e:
                        pass # we swallow the exception quietly, bad practice.
                    break
            if not mo:
                self.do_HEAD(404)
        else:
            self.do_AUTHHEAD()
            pass
