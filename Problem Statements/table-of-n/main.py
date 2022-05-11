import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        table_var = 5
        responseString = ""
        for i in range(1, 11):
            table = "{} * {} = {}".format(table_var, i, table_var*i)
            responseString = responseString + "<h4>{}</h4>".format(table)
        self.response.out.write(responseString)
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
