# Description
This is a simple web-based application which shows some nearest place according to given location. For built this applicaiton I make my own API used google maps Python Client library.

URL: http://127.0.0.1:8000 </br>
API: http://127.0.0.1:8000/api/location


# Requirements
```
    Python
    A Google Maps API key
```
    
# Installation
```
    $ pip install Django
    $ pip install djangorestframework
    $ pip install -U googlemaps 
    $ pip install requests
```

# Note
Please change the Google Maps API Key otherwise, it won't work. To change Google Maps API Key go to  ```myapp->api->views->line(17)->my_api_key``` change ```my_api__key``` value.

# Demo
![ScreenRecording7-22-201912-4](https://user-images.githubusercontent.com/16104417/61612415-58f8c300-ac80-11e9-8859-b2ad34c1eef8.gif)

