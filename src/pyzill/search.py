from typing import Any, List
from curl_cffi import requests
import json


def for_sale(
    pagination: int,
    search_value: str,
    min_beds: int,
    max_beds: int,
    min_bathrooms: int,
    max_bathrooms: int,
    min_price: int,
    max_price: int,
    ne_lat: float,
    ne_long: float,
    sw_lat: float,
    sw_long: float,
    zoom_value: int,
    proxy_url: str | None = None,
) -> dict[str, Any]:
    """get results of the listing that are for sale, you will get a dictionary with the keywords
    mapResults and listResults, use mapResults which contains all the listings from all paginations
    listResults is more for the right side bar that you see when searching on zillow. 
    Be aware the the maximum size of mapResults is 500 so if you get results with size 500, so if you want 
    to get the whole result frm a particular area, you need to play with the zoom, or the coordinates.
    Even if you try to paginate over all results, it won't work even if you use mapResults or listResults
    I would recomend not use pagination because you have all results(with 500 maximum) on mapResults
    Args:
        pagination (int): number of page in pagination
        ne_lat (float): ne latitude value
        ne_long (float): ne longitude value
        sw_lat (float): sw latitude value
        sw_long (float): sw longitude value
        sw_long (float): sw longitude value
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: listing of properties in JSON format
    """
    rent = {
		"sortSelection":  {"value": "globalrelevanceex"},
		"isAllHomes":  {"value": True},
	}
    return search(pagination,search_value,min_beds,max_beds,min_bathrooms,max_bathrooms,min_price,max_price,ne_lat,ne_long,sw_lat,sw_long,zoom_value,rent,proxy_url)

def for_rent(
    pagination: int,
    search_value: str,
    is_entire_place: bool,
    is_room: bool,
    min_beds: int,
    max_beds: int,
    min_bathrooms: int,
    max_bathrooms: int,
    min_price: int,
    max_price: int,
    ne_lat: float,
    ne_long: float,
    sw_lat: float,
    sw_long: float,
    zoom_value: int,
    proxy_url: str | None = None,
) -> dict[str, Any]:
    """get results of the listing that are for rent, you will get a dictionary with the keywords
    mapResults and listResults, use mapResults which contains all the listings from all paginations
    listResults is more for the right side bar that you see when searching on zillow. 
    Be aware the the maximum size of mapResults is 500 so if you get results with size 500, so if you want 
    to get the whole result frm a particular area, you need to play with the zoom, or the coordinates.
    Even if you try to paginate over all results, it won't work even if you use mapResults or listResults
    I would recomend not use pagination because you have all results(with 500 maximum) on mapResults
    Args:
        pagination (int): number of page in pagination
        ne_lat (float): ne latitude value
        ne_long (float): ne longitude value
        sw_lat (float): sw latitude value
        sw_long (float): sw longitude value
        sw_long (float): sw longitude value
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: listing of properties in JSON format
    """
    rent = {
		"sortSelection":  {"value": "priorityscore"},
		"isNewConstruction":  {"value": False},
		"isForSaleForeclosure":  {"value": False},
		"isForSaleByOwner":  {"value": False},
		"isForSaleByAgent":  {"value": False},
		"isForRent":  {"value": True},
		"isComingSoon":  {"value": False},
		"isAuction":  {"value": False},
		"isAllHomes":  {"value": True},
	}
    if is_room:
        rent["isRoomForRent"] = {"value": True}
    if not is_entire_place:    
        rent["isEntirePlaceForRent"] = {"value": False}
    return search(pagination,search_value,min_beds,max_beds,min_bathrooms,max_bathrooms,min_price,max_price,ne_lat,ne_long,sw_lat,sw_long,zoom_value,rent,proxy_url)

def sold(
    pagination: int,
    search_value: str,
    min_beds: int,
    max_beds: int,
    min_bathrooms: int,
    max_bathrooms: int,
    min_price: int,
    max_price: int,
    ne_lat: float,
    ne_long: float,
    sw_lat: float,
    sw_long: float,
    zoom_value: int,
    proxy_url: str | None = None,
) -> dict[str, Any]:
    """get results of the listing that were sold, you will get a dictionary with the keywords
    mapResults and listResults, use mapResults which contains all the listings from all paginations
    listResults is more for the right side bar that you see when searching on zillow. 
    Be aware the the maximum size of mapResults is 500 so if you get results with size 500, so if you want 
    to get the whole result frm a particular area, you need to play with the zoom, or the coordinates.
    Even if you try to paginate over all results, it won't work even if you use mapResults or listResults
    I would recomend not use pagination because you have all results(with 500 maximum) on mapResults
    Args:
        pagination (int): number of page in pagination
        ne_lat (float): ne latitude value
        ne_long (float): ne longitude value
        sw_lat (float): sw latitude value
        sw_long (float): sw longitude value
        sw_long (float): sw longitude value
        proxy_url (str | None, optional): proxy URL for masking the request. Defaults to None.

    Returns:
        dict[str, Any]: listing of properties in JSON format
    """
    rent = {
		"sortSelection":  {"value": "globalrelevanceex"},
		"isNewConstruction":  {"value": False},
		"isForSaleForeclosure":  {"value": False},
		"isForSaleByOwner":  {"value": False},
		"isForSaleByAgent":  {"value": False},
		"isForRent":  {"value": False},
		"isComingSoon":  {"value": False},
		"isAuction":  {"value": False},
		"isAllHomes":  {"value": True},
		"isRecentlySold":  {"value": True},
	}
    return search(pagination,search_value,min_beds,max_beds,min_bathrooms,max_bathrooms,min_price,max_price,ne_lat,ne_long,sw_lat,sw_long,zoom_value,rent,proxy_url)
    
def search(
    pagination: int,
    search_value: str,
    min_beds: int,
    max_beds: int,
    min_bathrooms: int,
    max_bathrooms: int,
    min_price: int,
    max_price: int,
    ne_lat: float,
    ne_long: float,
    sw_lat: float,
    sw_long: float,
    zoom_value: int,
    filter_state: dict[str, Any],
    proxy_url: str | None = None,
) -> dict[str, Any]:
    """get results of the listing of the given page number

    Args:
        pagination (int): number of page in pagination
        ne_lat (float): ne latitude value
        ne_long (float): ne longitude value
        sw_lat (float): sw latitude value
        sw_long (float): sw longitude value
        sw_long (float): sw longitude value
        filter_state (dict[str, Any]): input data for making the search
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
        "origin": "https://www.zillow.com",
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
            "isMapVisible": True,
            "isListVisible": True,
            "mapBounds": {
                "north": ne_lat,
                "east": ne_long,
                "south": sw_lat,
                "west": sw_long,
            },
            "filterState": filter_state,
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
    if search_value is not None:
        inputData["searchQueryState"]["usersSearchTerm"]=search_value

    if min_beds is not None or  max_beds is not None:
        beds = {}
        if min_beds is not None:
            beds["min"] = min_beds
        if max_beds is not None:
            beds["max"] = max_beds
        inputData["searchQueryState"]["filterState"]["beds"] = beds

    if min_bathrooms is not None or  max_bathrooms is not None:
        baths = {}
        if min_bathrooms is not None:
            baths["min"] = min_bathrooms
        if max_bathrooms is not None:
            baths["max"] = max_bathrooms
        inputData["searchQueryState"]["filterState"]["baths"] = baths

    if min_price is not None or  max_price is not None:
        price = {}
        if min_price is not None:
            price["min"] = min_price
        if max_price is not None:
            price["max"] = max_price
        inputData["searchQueryState"]["filterState"]["price"] = price

    proxies = {"http": proxy_url, "https": proxy_url} if proxy_url else None
    response = requests.put(
        url="https://www.zillow.com/async-create-search-page-state",
        json=inputData,
        headers=headers,
        proxies=proxies,  
        impersonate="chrome124",
    )
    data = response.json()
    return data.get("cat1", {}).get("searchResults", {})