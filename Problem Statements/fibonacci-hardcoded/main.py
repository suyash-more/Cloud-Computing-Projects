import webapp2

def Fibonacci(n):
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

class MainPage(webapp2.RequestHandler):
    def get(self):
        n = 8
        responseString = ""
        for i in range(0, n):
            responseString = responseString + "<h4>{} -> {}</h4>".format(i, Fibonacci(i))
        self.response.out.write(responseString)
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
