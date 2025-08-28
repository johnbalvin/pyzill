
import pyzill
import json
proxy_url = pyzill.parse_proxy("premium.residential.proxyrack.net","9000","masamasa-country-US","G7NR8PY-6UUOGDK-B3KHXDU-JLMUNR7-IXHHRVL-0N0MR6S-AX0ESBN")
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

results_rent = pyzill.for_rent(pagination, 
              search_value="",is_entire_place=False,is_room=True,
              min_beds=1,max_beds=None,
              min_bathrooms=None,max_bathrooms=None,
              min_price=10000,max_price=None,
              ne_lat=ne_lat,ne_long=ne_long,sw_lat=sw_lat,sw_long=sw_long,
              zoom_value=15,
              proxy_url=proxy_url)
jsondata_rent = json.dumps(results_rent)
f = open("./jsondata_rent2.json", "w")
f.write(jsondata_rent)
f.close()