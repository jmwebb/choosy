## Attributes in yelp data that can be used for choosing:
### categories
categories[0][alias] and categories[0][title]   
categories[1][alias] and categories[1][title]   
categories[2][alias] and categories[2][title]   
``` 
We can extract all different categories and pick randomly from them to design the questions.
This is the most important that we can use with limited data.
```
### price
$  
$$  
$$$  
$$$$  

### rating
5  
4.5  
4  

### review_count
different numbers represent different popularity, and may also have a relation with waiting time
```
There's a script called yell, which can extract review texts along with photos from one user.
Maybe we can use that, although it requires mannualy operations.
```
[yell](https://github.com/tmcw-up-for-adoption/yell)
### transaction
for special requirements like reservation, delivery and pick up

### is_closed
definitely false

### distance(not now)
HTML5 getCurrentLocation() method can be used in app to get user's location
```
<script>
var x = document.getElementById("demo");
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}
function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude; 
}
</script>
```

Google map parking structure API
retuan: json file of parking structure information near selected coordinates.
```
https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=lat,longt&radius=500&types=parking&sensor=false&key=APIKEY
```

Calculate distance(mile) from two sets of coordinates
```
from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...

```
