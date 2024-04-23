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
results = pyzill.Search_all(ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
details_data = []
progress = 1
jsondata = json.dumps(results)
f = open("results.json", "w")
f.write(jsondata)
f.close()
for result in results[:3]:
    data = pyzill.Get_from_property_id(result["zpid"],"")
    details_data.append(data)
    print("len results: ",progress, len(results))
    progress=progress+1
    
details_data_json = json.dumps(details_data)
f = open("details_data.json", "w")
f.write(details_data_json)
f.close()
```

```Python
import pyzill
import json
property_url="https://www.zillow.com/homedetails/858-Shady-Grove-Ln-Harrah-OK-73045/339897685_zpid/"
data = pyzill.Get_from_property_url(property_url,"")
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```

```Python
import pyzill
import json
property_id=2056016566
data = pyzill.Get_from_property_url(property_id,"")
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()
```
