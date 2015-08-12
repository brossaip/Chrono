import webapp2

class MainPage( webapp2.requestHandler ):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello Jep!')
        
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ], debug = True)