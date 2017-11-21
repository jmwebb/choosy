import urllib2
import json
import random
from firebase import firebase
import copy

default_query = "Los Angeles"
firebase = firebase.FirebaseApplication('https://projectfor551.firebaseio.com/', None)

def uploadB(query="losangeles", term="restaurants"):  #For uploading to firebase
    """
    upload data on 1000 restaurants searched by conditions
    :param query: optional, default value = "losangeles", case insensitive
    :param term: optional, default value = "restaurants"
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
        final_url = "https://api.yelp.com/v3/businesses/search?" + "term=" + term + "&location=" + location + "&limit=50" + "&sort_by_rating" + "&offset=" + str(i)
        request = urllib2.Request(final_url, headers=request_headers)
        json_obj = urllib2.urlopen(request)
        data = json.load(json_obj)
        for k in range(0, 50):
            dt["businesses"].append(data["businesses"][k])
            firebase.put('/restaurants', '"%s"'%dt["businesses"][k+i]["id"], dt["businesses"][k+i])
        i = i + 50

def getcat():
    c = {}
    result = firebase.get('/restaurants', None)
    for k in result:
        for n in result[k]["categories"]:
            c.update({n["alias"]:n["title"]})
            firebase.put('/categories', '"%s"'%n["alias"],n["title"])
    rand1 = random.choice(c.keys())
    rand2 = random.choice(c.keys())
    print "A:"+ rand1, "B:"+ rand2
    print c
    
def makeset():
    s = []
    result = firebase.get('/restaurants', None)
    for k in result:
        lis = []
        if not s:
            s.append(set())
            s[0].add(result[k]["categories"][0]["alias"])
        for m in range(len(s)):
            lis2 = []
            for n in result[k]["categories"]:
                if n["alias"] in s[m]:
                    lis2.append(1)
                else:
                    lis2.append(0)
            if any(lis2):
                for f in result[k]["categories"]:
                    s[m].add(f["alias"])
                    lis.append(1)
            else:
                lis.append(0)
        if not any(lis):
            s.append(set())
            for n in result[k]["categories"]:
                s[-1].add(n["alias"])
                    
def divide():
    s = {}
    result = firebase.get('/restaurants', None)
    cate = firebase.get('/categories', None)
    for k in cate:
        cate[k] = []
    print cate
    for k in result:
        for n in result[k]["categories"]:
            cate['\"'+n["alias"]+'\"'].append(result[k]["id"])
    for n in cate:
        firebase.put('/cate', n, cate[n])

def filt(value):
    c = {}
    result = firebase.get('/restaurants', None)
    for k in result:
        for n in result[k]["categories"]:
            if value == n["alias"]:
                c.update({n["title"]:n["alias"]})

def choosy():
    cate = firebase.get('/cate', None)
    while(1): #Once one process is finished, start over again
        A = random.choice(cate.keys())
        B = random.choice(cate.keys())
        hischo=[] #This list contains history choice
        restlist = [] #This list contains restaurants that fulfill the choices made this time
        temp = "Restaurant"
        while(1):
            if hischo: #If hischo has elements
                restlist.append(cate[hischo[len(hischo)-1]])
                #print restlist
                commanre = set(restlist[0]).intersection(*restlist) #Find same restaurants in different categories
                catelist = []
                if len(commanre) == 0:
                    for n in commanre:
                        res = n
                    restName = firebase.get('restaurants/\"%s\"/name' %res, None)
                    print "\n" + restName + " is your best choice!"
                    break
                if len(commanre) == 1:
                    for n in commanre:
                        res =  n
                    restName = firebase.get('restaurants/\"%s\"/name' %res, None)
                    print "\n" + restName + " is your best choice!"
                    break
                for n in commanre:
                    catedict = firebase.get('restaurants/\"%s\"/categories' %n, None)
                    for m in catedict:
                        catelist.append('\"'+m["alias"] + '\"')
                cateset = set(catelist)
                #print "cateset is "+ str(cateset)
                for l in hischo:
                    #print l 
                    cateset.remove(l)
                if not cateset:
                    e = random.sample(temp,1)
                    restName = firebase.get('restaurants/\"%s\"/name' %e[0], None)
                    print "\n" + restName + " is your best choice!"
                    print "If you want more, please continue!\n"
                    break
                temp = commanre

            lis = []
            print A, B
            print "Choose A or B"
            choice = raw_input()
            if choice == "A" or choice == "a":
                print "You choose A"
                hischo.append(A)
                tempcate = copy.deepcopy(cate)
                for n in hischo:
                    tempcate.pop(n)
                if len(cate[A]) == 1:
                    st = ""
                    for i in cate[A]:
                        st = st + i
                    restName = firebase.get('restaurants/\"%s\"/name' %st, None)
                    print "\n" + restName + " is your best choice!"
                    break 
                for x in hischo:
                    for rest in cate[x]:
                        for n in tempcate:
                            if rest in cate[n]:
                                lis.append(n) 
                    
                #print lis
                if len(lis)>=2:
                    sublist = random.sample(range(0,len(lis)),2)
                    #print sublist
                    if lis[sublist[0]] not in hischo and lis[sublist[1]] not in hischo:
                        A = lis[sublist[0]]
                        B = lis[sublist[1]]
                elif len(lis)==1:
                    ranres = random.choice(cate[A])
                    restName = firebase.get('restaurants/\"%s\"/name' %ranres, None)
                    print "\n" + restName + " is your best choice!"
                    break
                elif len(lis)==0:
                    ranres = random.choice(cate[A])
                    restName = firebase.get('restaurants/\"%s\"/name' %ranres, None)
                    print "\n" + restName + " is your best choice!"
                    break
            elif choice == "B" or choice == "b":
                print "you choose B"
                hischo.append(B)
                tempcate = copy.deepcopy(cate)
                tempcate.pop(B)
                if len(cate[B]) == 1:
                    st = ""
                    for i in cate[B]:
                        st = st + i
                    restName = firebase.get('restaurants/\"%s\"/name' %st, None)
                    print "\n" + restName + " is your best choice!"
                    break 
                for x in hischo:
                    for rest in cate[x]:
                        for n in tempcate:
                            if rest in cate[n]:
                                lis.append(n)
                if len(lis)>=2:
                    sublist = random.sample(range(0,len(lis)),2)
                    if lis[sublist[0]] not in hischo and lis[sublist[1]] not in hischo:
                        A = lis[sublist[0]]
                        B = lis[sublist[1]]
                elif len(lis)==1:
                    ranres = random.choice(cate[B])
                    restName = firebase.get('restaurants/\"%s\"/name' %ranres, None)
                    print "\n" + restName + " is your best choice!"
                    break
                elif len(lis)==0:
                    print "You're lucky"
                    ranres = random.choice(cate[B])
                    restName = firebase.get('restaurants/\"%s\"/name' %ranres, None)
                    print "\n" + restName + " is your best choice!"
                    break
            else:
                print "Let me find you others"
                break

def main():
    pass

"""
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