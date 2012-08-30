import webapp2
import time

class TimestampHandler(webapp2.RequestHandler):
    def get(self, format=None):
        timestamp = int(time.time())
        if format == 'xml':
            self.response.content_type = 'application/xml'
            self.response.write("<timestamp>%s</timestamp>" % timestamp)
        elif format == 'json':
            self.response.content_type = 'application/json'
            self.response.write('{"timestamp": "%s"}' % timestamp)
        else:
            self.response.content_type = 'text/plain'
            self.response.write(timestamp)
        self.response.headers['Cache-Control'] = 'public'
        self.response.md5_etag()


app = webapp2.WSGIApplication([
    ('/(\w+)?', TimestampHandler),
])