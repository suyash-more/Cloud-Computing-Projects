import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("hello world")
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
