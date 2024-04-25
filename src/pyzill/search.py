from typing import Any, List

from requests import put # type: ignore

def Search_all(
    ne_lat: float,
    ne_long: float,
    sw_lat: float,
    sw_long: float,
    zoom_value: int,
    proxy_url: str,
) -> List[dict[str, Any]]:
    """Traverse through pages of a listing in in bruteforce method

    Args:
        ne_lat (float): ne latitude value
        ne_long (float): ne longitude value
        sw_lat (float): sw latitude value
        sw_long (float): sw longitude value
        zoom_value (int): zoom value in map
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        List[dict[str, Any]]: list of properties in JSON format
    """
    all_results: List[dict[str, Any]] = []
    pagination = 0
    while True:
        pagination = pagination + 1
        results = search(
            pagination=pagination,
            ne_lat=ne_lat,
            ne_long=ne_long,
            sw_lat=sw_lat,
            sw_long=sw_long,
            zoom_value=zoom_value,
            proxy_url=proxy_url,
        )
        print("pagination: ", pagination, "len results: ", len(results))
        all_results.append(results)
        if not results:
            break
    return all_results


def Search_first_page(
    ne_lat: float,
    ne_long: float,
    sw_lat: float,
    sw_long: float,
    zoom_value: int,
    proxy_url: str | None = None,
) -> dict[str, Any]:
    """Get listings from first page

    Args:
        ne_lat (float): ne latitude value
        ne_long (float): ne longitude value
        sw_lat (float): sw latitude value
        sw_long (float): sw longitude value
        zoom_value (int): zoom value in map
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: listing of properties in JSON format
    """
    results = search(
        pagination=1,
        ne_lat=ne_lat,
        ne_long=ne_long,
        sw_lat=sw_lat,
        sw_long=sw_long,
        zoom_value=zoom_value,
        proxy_url=proxy_url,
    )
    return results


def search(
    pagination: int,
    ne_lat: float,
    ne_long: float,
    sw_lat: float,
    sw_long: float,
    zoom_value: int,
    proxy_url: str | None = None,
) -> dict[str, Any]:
    """get results of the listing of the given page number

    Args:
        pagination (int): number of page in pagination
        ne_lat (float): ne latitude value
        ne_long (float): ne longitude value
        sw_lat (float): sw latitude value
        sw_long (float): sw longitude value
        zoom_value (int): zoom value in map
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: listing of properties in JSON format
    """
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Language": "en",
        "Content-Type": "application/json",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    }
    inputData = {
        "searchQueryState": {
            "isMapVisible": False,
            "mapBounds": {
                "north": ne_lat,
                "east": ne_long,
                "south": sw_lat,
                "west": sw_long,
            },
            "filterState": {
                "sortSelection": {
                    "value": "globalrelevanceex",
                }
            },
            "isEntirePlaceForRent": True,
            "isRoomForRent": True,
            "isListVisible": True,
            "mapZoom": zoom_value,
            "pagination": {
                "currentPage": pagination,
            },
        },
        "wants": {
            "cat1": ["listResults", "mapResults"],
            "cat2": ["total"],
        },
        "requestId": 10,
        "isDebugRequest": False,
    }

    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    response = put(
        url="https://www.zillow.com/async-create-search-page-state",
        json=inputData,
        headers=headers,
        proxies=proxies,
    )
    data = response.json()
    return data.get("cat1", {}).get("searchResults", {}).get("listResults", {})
