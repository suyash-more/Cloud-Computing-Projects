import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            "error": ""
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        title = self.request.get('title')

        query_params = "?title={}".format(title)
        url = "https://ghibliapi.herokuapp.com/films" + query_params
        data = urllib.urlopen(url).read().decode("UTF-8")
        data = json.loads(data)
        # location = data.get()
        template_values = {
            "title": data[0]['title'],
            "director": data[0]['director'],
            "producer": data[0]['producer'],
            "release_date": data[0]['release_date'],
            "url": data[0]['url']
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
