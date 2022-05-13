import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

    def post(self):
        pincode = self.request.get('zipCode')
        if not pincode.isnumeric() or not len(pincode) == 6:
            template_values = {
                "error": "Incorrect Pin Code (String / False Code entered)"
            }
            path = os.path.join(os.path.dirname(__file__), 'index.html')
            return self.response.out.write(template.render(path, template_values))
        url = "https://api.postalpincode.in/pincode/" + pincode
        data = urllib.urlopen(url).read()
        data = json.loads(data)
        if(data[0]['Status'] == 'Success'):
            post_office = data[0]['PostOffice'][0]['State']
            name = data[0]['PostOffice'][0]['Name']
            block = data[0]['PostOffice'][0]['Block']
            district = data[0]['PostOffice'][0]['District']
            template_values = {
                "post_office": post_office,
                "name": name,
                "block": block,
                "district": district
            }
            path = os.path.join(os.path.dirname(__file__), 'results.html')
            self.response.out.write(template.render(path, template_values))
        else:
            template_values = {}
            path = os.path.join(os.path.dirname(__file__), 'error.html')
            self.response.out.write(template.render(path, template_values))


app = webapp2.WSGIApplication([('/', MainPage)], debug=True)