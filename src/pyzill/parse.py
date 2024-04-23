from bs4 import BeautifulSoup
from pyzill.utils import remove_space
import json
import html

def parse_body_details_wrapper(body:str):
    soup = BeautifulSoup(body, 'html.parser')
    selections=soup.select("#__NEXT_DATA__")
    if len(selections)==0:
        return {}
    htmlData = soup.select("#__NEXT_DATA__")[0].getText()
    htmlData = remove_space(html.unescape(htmlData))
    data = json.loads(htmlData)
    property=data["props"]["pageProps"]["componentProps"]["gdpClientCache"]
    property = json.loads(property)
    for data in property.values():
        if "property" in data:
            return data["property"]
    return {}