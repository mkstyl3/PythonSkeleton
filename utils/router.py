import re
import json
import falcon

from config.routes import *


class Router:
    def __init__(self, app):
        app.req_options.auto_parse_form_urlencoded = True  # form "x-www-form-urlencoded" if not lib falcon-multipart
        for route in routes:
            app.add_route(route['path'], self)

    def on_post(self, req, resp):
        self.request(req, resp)

    def on_put(self, req, resp):
        self.request(req, resp)

    def on_get(self, req, resp):
        self.request(req, resp)

    def request(self, req, resp):
        try:
            for route in routes:
                if route['method'] == req.method.lower() and route['path'] == req.path:
                    controller, method = route['resource'].split(':')
                    response = getattr(eval(controller)(), method)(self.getParams(req))
                    resp.body = response if isinstance(response, str) else str(response)
                else:
                    resp.status = falcon.HTTP_405
        except Exception as e:
            resp.body = str(e)

    def getParams(self, req):
        params = dict()
        if req.method == 'GET':
            params = req.params
        elif req.method == 'POST':
            params = req.params
            if len(params) == 0:
                post = req.bounded_stream.read(req.content_length or 0).decode('utf-8')
                if post.find('&') != -1:  # form "x-www-form-urlencoded" if not lib falcon-multipart
                    post = '{' + re.sub(r'(\w+)=(\w+)', r'"\1":"\2"', post.replace('&', ',')) + '}'
                elif post.find('form-data') != -1:  # form type " form-data "
                    post = '{' + re.sub(r'(.*)(\r\n)(.*)("[\w\d]*")([\r\n]{0,})([\w\d]*)([\r\n]{0,})', r'\4:"\6",', post.replace('&', ',')) + '}'
                    post = post[0:-46] + '}'
                params = json.loads(post)
        return params
