import pyzill
import json

#use rotating residential proxies
proxy_url = pyzill.parse_proxy("[proxy_ip or proxy_domain]","[proxy_port]","[proxy_username]","[proxy_password]")
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
              search_value="",
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