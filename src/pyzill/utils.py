from re import compile
from typing import Tuple

regex_space = compile(r"[\s ]+")
regx_price = compile(r"\d+")


def remove_space(value: str) -> str:
    """remove unwanted spaces in given string

    Args:
        value (str): input string with unwanted spaces

    Returns:
        str: string with single spaces
    """
    return regex_space.sub(" ", value.strip())


def get_nested_value(dic, key_path, default=None):
    keys = key_path.split(".")
    current = dic
    for key in keys:
        current = current.get(key, {})
        if current == {} or current is None:
            return default
    return current


def parse_price_symbol(price_raw: str) -> Tuple[float, str]:
    """Takes price string and parses price as integer and currency symbol

    Args:
        price_raw (str): Eg "$ 56"

    Returns:
        Tuple[float, str]: Eg (56, "$")
    """

    extracted_price, currency = 0.0, ""
    price_raw = price_raw.replace(",", "")
    price_number_match = regx_price.search(price_raw)
    if price_number_match:
        price_number = price_number_match.group(0)
        currency = price_raw.replace(price_number, "").replace(" ", "").replace("-", "")
        extracted_price = float(price_number)
        if price_raw.startswith("-"):
            extracted_price *= -1
    return extracted_price, currency
