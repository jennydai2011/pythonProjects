import requests
from bs4 import BeautifulSoup
import re
import googlemaps,json

gmaps = googlemaps.Client(key='AIzaSyC6a8kgSNoxL6FX6AgGrC0kVXCZdBhUxgw')

r = requests.get('https://www.kijiji.ca/b-garage-sale-yard-sale/edmonton/c638l1700203')
soup = BeautifulSoup(r.content, "html.parser")
links = soup.select("a[href]")

addresslist = []
for link in links:   
    try:
        hreft = link.get("href")        
    except:
        pass
    
    if "v-garage-sale" in hreft:           
        #print("item index:"+str(indx))                   
        item_url = 'https://www.kijiji.ca'+hreft+'?enableSearchNavigationFlag=true'
        #print("item_url:"+item_url)
        itemr = requests.get(item_url)                        
        itemsoup = BeautifulSoup(itemr.content, "html.parser")            
        
        try:
            itemlocations = itemsoup.select("span[class*=address]")
            address = itemlocations[0].contents[0]
            if "T6" in address:
                addresslist.append(address)               
        except:
            pass

print(" addresslist len:"+ str(len(addresslist)))   
 
f = open('kijiji-garagesale-geo.txt','w')
for address in addresslist:
    #add mark in a map,to file
    if "T6" in address and "NW" in address:    
        # Geocoding an address
        print("machted address:"+address)
        geocode_result = gmaps.geocode(address) 
        #jsonresult = json.load(geocode_result) 
        geolocation_result = geocode_result[0]['geometry']['location']         
        print("machted address geolocation:"+str(geolocation_result))      
        f.write(str(geolocation_result)+'\n')
f.close()
