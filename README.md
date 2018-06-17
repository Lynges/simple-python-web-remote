# simple-python-web-remote
Using the http.server module to facilitate remote control vie GET requests
The aim is to a very simple setup for triggering updates or simply letting a system know that an event has occured, but using only http GET requests.

### Instructions
Import and subclass `RemoteControlHander`:

```python
from webremote import RemoteControlHander

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
```

`keystring` is the auth string for all requests. Auth is not optional.

`set_urls` is called during init and must set `self.urls` to a list of two-tuples with a regex pattern first and a function indentifier second.

urls are evaluated from top to bottom with `re.fullmatch()`. Parsing of get parameters is not implimented, but could be. Inside your own functions you will have access to the entire Handler object as described in the (python docs)[https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler]

The response has already been went when your custom code is run, so no rush to get done, but things like redirects and custom responses are not possible.

Now you are ready to run the server like so:

```python
from http.server import HTTPServer

def run(server_class=HTTPServer, handler_class=TestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
```
