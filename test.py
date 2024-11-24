import pyzill
import json

#use residential proxies
proxy_url = pyzill.parse_proxy("[proxy_ip or proxy_domain]","[proxy_port]","[proxy_username]","[proxy_password]")
property_id=2056016566
data = pyzill.get_from_property_id(property_id,proxy_url)
jsondata = json.dumps(data)
f = open("details.json", "w")
f.write(jsondata)
f.close()