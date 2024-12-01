from html import unescape
from json import loads
from typing import Any

from bs4 import BeautifulSoup  # type: ignore

from pyzill.utils import remove_space,get_nested_value


def parse_body_home(body: bytes) -> dict[str, Any]:
    """parse HTML content to retrieve JSON data

    Args:
        body (bytes): HTML content of web page

    Returns:
        dict[str, Any]: parsed property information
    """
    componentProps = parse_body(body)
    data_raw = get_nested_value(componentProps,"gdpClientCache")
    property_json = loads(data_raw)
    parsed_data={}
    for data in property_json.values():
        if "property" in str(data):
            parsed_data = data.get("property")
    return parsed_data

def parse_body_deparments(body: bytes) -> dict[str, Any]:
    """parse HTML content to retrieve JSON data

    Args:
        body (bytes): HTML content of web page

    Returns:
        dict[str, Any]: parsed property information
    """
    componentProps = parse_body(body)
    department_json = get_nested_value(componentProps,"initialReduxState.gdp")
    return department_json

def parse_body(body: bytes) -> dict[str, Any]:
    """parse HTML content to retrieve JSON data

    Args:
        body (bytes): HTML content of web page

    Returns:
        dict[str, Any]: parsed property information
    """
    soup = BeautifulSoup(body, "html.parser")
    selection = soup.select_one("#__NEXT_DATA__")
    if selection:
        htmlData = selection.getText()
        htmlData = remove_space(unescape(htmlData))
        data = loads(htmlData)
        return get_nested_value(data,"props.pageProps.componentProps")