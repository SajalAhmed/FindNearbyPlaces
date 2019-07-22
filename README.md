# Description
This is a simple web-based application which shows some nearest place according to the given location. For build this application I make my own API used google maps python client library. This project can be done without API build. 


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
# How to run project locally
```
    1. Download the project.
    2. Go to FindNearbyPlaces folder
    3. Open CMD in FindNearbyPlaces location
    4. Run: python manage.py runserver
    5. Open the browser to view the project
    URL: http://127.0.0.1:8000
    API: http://127.0.0.1:8000/api/location
```

# Note
Please change the Google Maps API Key otherwise, it won't work. To change Google Maps API Key go to  ```myapp->api->views->line(17)->my_api_key``` change ```my_api__key``` value.

# Demo
![ScreenRecording7-22-201912-4](https://user-images.githubusercontent.com/16104417/61612415-58f8c300-ac80-11e9-8859-b2ad34c1eef8.gif)

