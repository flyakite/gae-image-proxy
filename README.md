
What is it?
-----------

A Google App Engine (python 2.7) proxy server to convert cross domain image to base64 and wrapped in a json object.
This is useful when you run into a canvas cross domain security problem. 
In your javascript, you can use modules that supports jsonp to get the json object. (e.g $.getJSON in jQuery)


How to use?
-----------

For example, resquest to 

    http://your-app-name.appspot.com/?url=http://path.to/image.jpg

returns something like
	
	{ 
		'height': 50, 
	  	'width' : 50, 
	  	'data'  : 'data:image/jpeg;base64,QWRarjgk4546asd...QWAsdf'
	}

You only need to change your-app-name in app.yaml and you are ready to go.


Licensed under the Apache License, Version 2.0 
