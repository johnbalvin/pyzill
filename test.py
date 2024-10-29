import pyzill
import json


def test1():
  #  property_id=2058520213
    
    property_id=75828885
    data = pyzill.get_from_property_id(property_id,"")
    jsondata = json.dumps(data)
    f = open("./details.json", "w")
    f.write(jsondata)
    f.close()

test1()

def test2():
    property_url="https://www.zillow.com/homedetails/6453-Ficus-Ln-Lake-Worth-FL-33462/2068566820_zpid/"    
    data = pyzill.get_from_property_url(property_url,"")
    jsondata = json.dumps(data)
    f = open("./details2.json", "w")
    f.write(jsondata)
    f.close()
test2()

def test3():
    ne_lat = 47.76725314073866
    ne_long = -122.15539952490977
    sw_lat = 47.67128302452179
    sw_long =-122.3442270395582
    zoom_value = 2
    results_sold = pyzill.sold(1, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
    results_sale = pyzill.for_sale(1, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
    results_rent = pyzill.for_rent(1, ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
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