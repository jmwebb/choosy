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

### distance
may use this
