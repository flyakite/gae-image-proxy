# -*- coding: utf-8 -*-

import logging
import json
import base64
import cStringIO
import urllib

from google.appengine.api import images, urlfetch
import webapp2

image_types = {
              images.JPEG : 'image/jpeg',
              images.PNG  : 'image/png',
              images.GIF  : 'image/gif',
}

class ImageToJsonHandler(webapp2.RequestHandler):
    def write_json(self, params):
        data = json.dumps(params)
        callback = self.request.get('callback')
        if callback:
            data = callback + '(' + data + ');'
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(data)

        
    def get(self):
        
        url = self.request.get('url')
        if not url:
            self.abort(404)
            
        result = urlfetch.fetch(urllib.unquote(url))
        if result.status_code != 200:
            logging.error('Image Not Found, status %s' % result.status_code)
            self.abort(404)

        img = cStringIO.StringIO(result.content)
        image = images.Image(img.getvalue())
        prefix = "data:" + image_types.get(image.format) + ";base64,"
        b64image = base64.b64encode(img.getvalue())
        params = {
            "width": image.width,
            "height": image.height,
            "data": prefix + b64image
        }

        self.write_json(params)

                
                
                
                
        
        