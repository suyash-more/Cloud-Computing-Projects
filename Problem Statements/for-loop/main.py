import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = "Bob"
        seat= "FJK123"
        department = "IT"
        responseString = ""
        for _ in range(5):
            responseString = responseString + "<br><h1>Name : {}, Seat: {}, Department: {}</h1>".format(name,seat,department) 
        self.response.out.write(responseString)
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
