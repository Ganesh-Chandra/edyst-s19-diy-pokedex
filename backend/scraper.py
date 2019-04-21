import requests
ur="https://pokeapi.co/api/v2/pokemon/"
fulldata={}
for id in range(1,152):
    jdata=requests.get(url=ur+str(id)).json()
    fulldata[id]=[jdata['id'],jdata['name'],jdata['sprites']['front_default']]
db=open("backend/data.txt",'w')
db.write(str(fulldata))
