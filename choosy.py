import urllib2
import json
from firebase import firebase

default_query = "Los Angeles"
firebase = firebase.FirebaseApplication('https://projectfor551.firebaseio.com/', None)

def uploadB(query="losangeles", term="restaurants"):  #For uploading to firebase
    """
    upload data on 1000 restaurants searched by conditions
    :param query: optional, location, default value = "losangeles", case insensitive
    :param term: optional, business types, default value = "restaurants"
    """
    request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "http://usc.edu",
    "Connection": "keep-alive",
    "Authorization": "Bearer _3DbLZAYDi1duBJihSnmHo3XyNIxWWZTI-TwlqaF7t8G2cEB5G5FzUMcKUX3mbixySS0aimgIq1iHifTPjl-etvmlTRDwYCUs9l-m2Ze7K-Wm5ge5n-EVIEEr828WXYx"
    }
    i = 0 #times, each time only 50 data
    dt = {"businesses":[]} # to store data retrived each time
    while i < 1000:
        location = query.replace(' ', '')
        final_url = "https://api.yelp.com/v3/businesses/search?" +"term=" + term + "&location=" + location + "&limit=50" + "&sort_by_rating" + "&offset=" + str(i)
        request = urllib2.Request(final_url, headers= request_headers)
        json_obj=urllib2.urlopen(request)
        data = json.load(json_obj)
        for k in range(0,50):
            dt["businesses"].append(data["businesses"][k])
            firebase.put('/'+terms,'"%s"'%dt["businesses"][k+i]["id"],dt["businesses"][k+i])
        i = i + 50

"""
def yelpApi(query):  #for testing
    request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "http://thewebsite.com",
    "Connection": "keep-alive",
    "Authorization": "Bearer _3DbLZAYDi1duBJihSnmHo3XyNIxWWZTI-TwlqaF7t8G2cEB5G5FzUMcKUX3mbixySS0aimgIq1iHifTPjl-etvmlTRDwYCUs9l-m2Ze7K-Wm5ge5n-EVIEEr828WXYx"
    }
    location = query.replace(' ', '')
    final_url = "https://api.yelp.com/v3/businesses/search?" +"location=" + location+"&limit=50"
    request = urllib2.Request(final_url, headers= request_headers)
    json_obj=urllib2.urlopen(request)
    data = json.load(json_obj)
    for item in data['businesses']:
        print item["name"]
        print item["rating"]
        print item["review_count"]
#        print item["price"]

def getB(query):  #Downloading json file to local
    request_headers = {
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "http://thewebsite.com",
    "Connection": "keep-alive",
    "Authorization": "Bearer _3DbLZAYDi1duBJihSnmHo3XyNIxWWZTI-TwlqaF7t8G2cEB5G5FzUMcKUX3mbixySS0aimgIq1iHifTPjl-etvmlTRDwYCUs9l-m2Ze7K-Wm5ge5n-EVIEEr828WXYx"
    }
    i = 0
    dt = {"businesses":[]}
    ls = []
    while i < 1000:
        location = query.replace(' ', '')
        final_url = "https://api.yelp.com/v3/businesses/search?" +"term=restaurants&location=" + location + "&limit=50" + "&sort_by_rating" + "&offset=" + str(i)
        request = urllib2.Request(final_url, headers= request_headers)
        json_obj=urllib2.urlopen(request)
        data = json.load(json_obj)
        for k in range(0,50):
            dt["businesses"].append(data["businesses"][k])
        i = i + 50
        dt2 = json.dumps(dt)
        with open ("yelpb.json", "a") as f:
            f.write(dt2)
"""

def main():
    pass
