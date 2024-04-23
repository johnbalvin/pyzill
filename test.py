import pyzill
import json


def test1():
    property_id=2056016566
    data = pyzill.Get_from_property_id(property_id,"")
    jsondata = json.dumps(data)
    f = open("./details.json", "w")
    f.write(jsondata)
    f.close()


def test2():
    ne_lat = 47.76725314073866
    ne_long = -122.15539952490977
    sw_lat = 47.67128302452179
    sw_long =-122.3442270395582
    zoom_value = 2
    results = pyzill.Search_all(ne_lat,ne_long,sw_lat,sw_long,zoom_value, "")
    jsondata = json.dumps(results)
    f = open("./search.json", "w")
    f.write(jsondata)
    f.close()

def test2():
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

test2()