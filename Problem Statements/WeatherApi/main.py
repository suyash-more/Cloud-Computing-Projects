import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
                "error" : ""
            }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        latitude = self.request.get('latitude')
        longitude = self.request.get('longitude')
        hourly = self.request.get('hourly')
        daily = self.request.get('daily')
        timezone = self.request.get('timezone')
        try:
            float(latitude)
        except ValueError:
            template_values = {
                "error" : "latitude is not a float value (alphabets must not be included)"
            }
            path = os.path.join(os.path.dirname(__file__), 'index.html')
            return self.response.out.write(template.render(path, template_values))
        try:
            float(longitude)
        except ValueError:
            template_values = {
                "error" : "longitude is not a float value (alphabets must not be included)"
            }
            path = os.path.join(os.path.dirname(__file__), 'index.html')
            return self.response.out.write(template.render(path, template_values))
        query_params = "?latitude={}&longitude={}&hourly={}&daily={}&timezone={}".format(latitude, longitude, hourly, daily, timezone)
        url = "https://api.open-meteo.com/v1/forecast/"+ query_params
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        # location = data.get()
        template_values = {
            "location": data
        }
        path = os.path.join(os.path.dirname(__file__), 'results.html')
        self.response.out.write(template.render(path, template_values))
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)