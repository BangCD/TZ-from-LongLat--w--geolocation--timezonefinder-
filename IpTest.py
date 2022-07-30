import urllib.request
import json


ips = ['94.208.120.202', '185.97.201.89','154.160.10.201']

latList=[]
longlist=[]
for ip in ips:
        with urllib.request.urlopen("https://geolocation-db.com/jsonp/"+ip) as url:
                data = url.read().decode()
                data = data.split("(")[1].strip(")")
                data=data.replace('"',"")
                print(data)
                
                print(type(data))
                dataList=data.split(",")
                print(dataList,end="")
                print("\n")
                lat=dataList[4].split(":")
                latList.append(lat[1])
                print("\n",lat,"\n")
                long=dataList[5].split(":")
                longlist.append(long[1])
                

for i in range(len(longlist)):
    print("Longitude: {0} Latitude: {1}\n ".format(longlist[i],latList[i]))
                
                
for i in range(len(longlist)):
        with urllib.request.urlopen("http://timezonefinder.michelfe.it/api/{0}_{1}_{2}".format(0,longlist[i],latList[i])) as url:
            tz=url.read().decode()
            print(tz)