# Zillow scraper in Python

## Overview
This project is an open-source tool developed in Python for extracting product information from Zillow. It's designed to be easy to use, making it an ideal solution for developers looking for Zillow product data.

## Features
- Full search support
- Extracts detailed product information from Zillow
- Implemented in Python just because it's popular
- Easy to integrate with existing Python projects

### Important
- Use rotating residential proxies, zillow will block if you make multiple requests with the same IP, 

### Install

```bash
$ pip install pyzill
```
## Examples

```Python
import pyzill
import json
ne_lat = 38.602951833355434
ne_long = -87.22283859375
sw_lat = 23.42674607019482
sw_long = -112.93084640625
pagination = 1
#pagination is for the list that you see at the right when searching
#you don't need to iterate over all the pages because zillow sends the whole data on mapresults at once on the first page
#however the maximum result zillow returns is 500, so if mapResults is 500
#try playing with the zoom or moving the coordinates, pagination won't help because you will always get at maximum 500 results
pagination = 1
proxy_url = pyzill.parse_proxy("[proxy_ip or proxy_domain]","[proxy_port]","[proxy_username]","[proxy_password]")
results_sold = pyzill.sold(pagination, 
              search_value="miami",
              min_beds=1,max_beds=1,
              min_bathrooms=None,max_bathrooms=None,
              min_price=10000,max_price=None,
              ne_lat=ne_lat,ne_long=ne_long,sw_lat=sw_lat,sw_long=sw_long,
              zoom_value=5,
              proxy_url=proxy_url)
              
results_sale = pyzill.for_sale(pagination, 
              search_value="",
              min_beds=None,max_beds=None,
              min_bathrooms=3,max_bathrooms=None,
              min_price=None,max_price=None,
              ne_lat=ne_lat,ne_long=ne_long,sw_lat=sw_lat,sw_long=sw_long,
              zoom_value=10,
              proxy_url=proxy_url)

results_rent = pyzill.for_rent(pagination, 
              search_value="",is_entire_place=False,is_room=True,
              min_beds=1,max_beds=None,
              min_bathrooms=None,max_bathrooms=None,
              min_price=10000,max_price=None,
              ne_lat=ne_lat,ne_long=ne_long,sw_lat=sw_lat,sw_long=sw_long,
              zoom_value=15,
              proxy_url=proxy_url)
jsondata_sold = json.dumps(results_sold)
jsondata_sale = json.dumps(results_sale)
jsondata_rent = json.dumps(results_rent)
f = open("./jsondata_sold.json", "w")
f.write(jsondata_sold)
f.close()
f = open("./jsondata_sale.json", "w")
f.write(jsondata_sale)
f.close()
f = open("./jsondata_rent.json", "w")
f.write(jsondata_rent)
f.close()
```
# For homes

```Python
import pyzill
import json
property_url="https://www.zillow.com/homedetails/858-Shady-Grove-Ln-Harrah-OK-73045/339897685_zpid/"
proxy_url = pyzill.parse_proxy("[proxy_ip or proxy_domain]","[proxy_port]","[proxy_username]","[proxy_password]")
data = pyzill.get_from_home_url(property_url,proxy_url)
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```

```Python
import pyzill
import json
property_id=2056016566
proxy_url = pyzill.parse_proxy("[proxy_ip or proxy_domain]","[proxy_port]","[proxy_username]","[proxy_password]")
data = pyzill.get_from_home_id(property_id,proxy_url)
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```

# For departments

```Python
import pyzill
import json
property_url="https://www.zillow.com/apartments/kissimmee-fl/the-nexus-at-overbrook/9DSWrh/"
proxy_url = pyzill.parse_proxy("[proxy_ip or proxy_domain]","[proxy_port]","[proxy_username]","[proxy_password]")
data = pyzill.get_from_deparment_url(property_url,proxy_url)
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```

```Python
import pyzill
import json
property_id="CgKZT4"
proxy_url = pyzill.parse_proxy("[proxy_ip or proxy_domain]","[proxy_port]","[proxy_username]","[proxy_password]")
data = pyzill.get_from_deparment_id(property_id,proxy_url)
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```