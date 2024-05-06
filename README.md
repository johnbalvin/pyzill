# Zillow scraper in Python

## Overview
This project is an open-source tool developed in Python for extracting product information from Zillow. It's designed to be easy to use, making it an ideal solution for developers looking for Zillow product data.

## Features
- Full search support
- Extracts detailed product information from Zillow
- Implemented in Python just because it's popular
- Easy to integrate with existing Python projects

### Install

```bash
$ pip install pyzill
```
## Examples

```Python
import pyzill
import json
ne_lat = 47.76725314073866
ne_long = -122.15539952490977
sw_lat = 47.67128302452179
sw_long =-122.3442270395582
zoom_value = 2
#pagination is for the list that you see at the right when searching
#you don't need to iterate over all the pages because zillow sends the whole data on mapresults at once on the first page
#however the maximum result zillow returns is 500, so if mapResults is 500
#try playing with the zoom or moving the coordinates, pagination won't help because you will always get at maximum 500 results
pagination = 1 
results_sold = pyzill.sold(pagination, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
results_sale = pyzill.for_sale(pagination, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
results_rent = pyzill.for_rent(pagination, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
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

```Python
import pyzill
import json
property_url="https://www.zillow.com/homedetails/858-Shady-Grove-Ln-Harrah-OK-73045/339897685_zpid/"
data = pyzill.get_from_property_url(property_url,"")
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```

```Python
import pyzill
import json
property_id=2056016566
data = pyzill.get_from_property_id(property_id,"")
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```
