from html import unescape
from json import loads
from typing import Any

from bs4 import BeautifulSoup  # type: ignore

from pyzill.utils import remove_space,get_nested_value


def parse_body_details_wrapper(body: bytes) -> dict[str, Any]:
    """parse HTML content to retrieve JSON data

    Args:
        body (bytes): HTML content of web page

    Returns:
        dict[str, Any]: parsed property information
    """
    parsed_data: dict[str, Any] = {}
    soup = BeautifulSoup(body, "html.parser")
    selections = soup.select("#__NEXT_DATA__")
    if selections:
        htmlData = soup.select("#__NEXT_DATA__")[0].getText()
        htmlData = remove_space(unescape(htmlData))
        data = loads(htmlData)
        property_json =get_nested_value(data,"props.pageProps.componentProps.gdpClientCache")
        property_json = loads(property_json)
        for data in property_json.values():
            if "property" in str(data):
                parsed_data = data.get("property")
    return parsed_data
