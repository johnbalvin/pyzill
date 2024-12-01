from typing import Any
from curl_cffi import requests
from pyzill.parse import parse_body_home,parse_body_deparments

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}

def get_from_home_id(
    property_id: int, proxy_url: str | None = None
) -> dict[str, Any]:
    """Scrape data for property based on property ID from zillow

    Args:
        property_id (int): ID for any property from zillow
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: parsed property information
    """
    home_url = f"https://www.zillow.com/homedetails/any-title/{property_id}_zpid/"
    data = get_from_home_url(home_url, proxy_url)
    return data

def get_from_deparment_id(
    deparment_id: str, proxy_url: str | None = None
) -> dict[str, Any]:
    """Scrape data for property based on deparment ID from zillow

    Args:
        property_id (int): ID for any property from zillow
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: parsed property information
    """
    
    home_url = f"https://www.zillow.com/apartments/texas/the-lennox/{deparment_id}"
    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    response = requests.get(url=home_url, headers=headers, proxies=proxies, impersonate="chrome124")
    data = parse_body_deparments(response.content)
    return data

def get_from_deparment_url(
    deparment_url: int, proxy_url: str | None = None
) -> dict[str, Any]:
    """Scrape data for property based on deparment ID from zillow

    Args:
        property_id (int): ID for any property from zillow
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: parsed property information
    """
    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    response = requests.get(url=deparment_url, headers=headers, proxies=proxies, impersonate="chrome124")
    data = parse_body_deparments(response.content)
    return data

def get_from_home_url(home_url: str, proxy_url: str | None = None) -> dict[str, Any]:
    """Scrape given URL and parse home detail

    Args:
        home_url (str): URL for the property
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: parsed property information
    """
    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    response = requests.get(url=home_url, headers=headers, proxies=proxies, impersonate="chrome124")
    response.raise_for_status()
    data = parse_body_home(response.content)
    return data