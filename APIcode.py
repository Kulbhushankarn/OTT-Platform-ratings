import http.client
import json
from prettytable import PrettyTable
#for this running of code you must be install prettytable in your terminal "pip install prettytable"
conn = http.client.HTTPSConnection("ott-details.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "9bb5d2bd5emsh3ee83c63eb98159p1f27c2jsn8905f37ab9f6",
    'x-rapidapi-host': "ott-details.p.rapidapi.com"
    }

conn.request("GET", "/advancedsearch?start_year=1970&end_year=2020&min_imdb=6&max_imdb=7.8&genre=action&language=english&type=movie&sort=latest&page=1", headers=headers)

res = conn.getresponse()
data = res.read()

mydata=json.loads(data.decode("utf-8"))
k=mydata['results']
myheading=PrettyTable(['Title','Imdb Rating',"Released"])

for i in k:
    
    t=i['title']
    im=i['imdbrating']
    re=i['released']
    myheading.add_row([t,im,re])

print(myheading)    
