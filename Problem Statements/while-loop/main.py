import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        name = "Bob"
        seat= "FJK123"
        department = "IT"
        responseString = ""
        loop_variable = 5
        while loop_variable > 0:
            responseString = responseString + "<br><h1>Name : {}, Seat: {}, Department: {}</h1>".format(name, seat, department) 
            loop_variable = loop_variable - 1
        self.response.out.write(responseString)
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
