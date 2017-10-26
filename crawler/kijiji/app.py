import requests
from bs4 import BeautifulSoup
import re

r = requests.get('https://www.kijiji.ca/b-garage-sale-yard-sale/edmonton/c638l1700203')
#print(r.content)

soup = BeautifulSoup(r.content, "html.parser")

#print(soup.prettify())

# <a href="/v-garage-sale-yard-sale/edmonton/huge-moving-sale-west-edmonton/1305250116?enableSearchNavigationFlag=true" class="title enable-search-navigation-flag ">
#                                 Huge Moving Sale West Edmonton</a>
#  <a href="/v-garage-sale-yard-sale/edmonton/ladies-teen-age-girls-clothes/1305697574?enableSearchNavigationFlag=true" class="title enable-search-navigation-flag ">
#                                 LADIES &amp; TEEN AGE GIRLS  CLOTHES.</a>

#links = soup.find_all("a")
links = soup.select("a[href]")
#links = soup.find_all('a', href = re.compile(r'*garage\-sale'))
#print(links)

indx =0 
addresslist = []
for link in links:    
    #print(link.text)
   
        
    try:
        hreft = link.get("href")        
    except:
        pass
    
    #print(hreft)
    

    if "v-garage-sale" in hreft:  
        indx = indx +1         
        print("item index:"+str(indx))
        if indx > 2:
            exit
        print("<a href='%s'>%s</a>" %(link.get("href"), link.text))
        #hreft = link.get("href")
            
        item_url = 'https://www.kijiji.ca'+hreft+'?enableSearchNavigationFlag=true'
        print("item_url:"+item_url)
        itemr = requests.get(item_url)
                        
        itemsoup = BeautifulSoup(itemr.content, "html.parser")
            
        #print(itemsoup.prettify())
        try:
        #     #itemlocations = itemsoup.find_all("span", class=lambda value: value and value.startswith("address"))
        #     #itemlocations = itemsoup.find_all("span", class=re.compile("^address-"))
            itemlocations = itemsoup.select("span[class*=address]")
            #print(" location len:"+ str(len(itemlocations)))
            address = itemlocations[0].contents[0]
            addresslist.append(address)
            print(" location :"+ address)

            # for itemlocation in itemlocations:
            #     print("Address is:"+itemlocation.contents[0])
                
        except:
            pass


print(" addresslist len:"+ str(len(addresslist)))    
