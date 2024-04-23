import re

regex_space = re.compile(r'[\s ]+')
regx_price = re.compile(r'\d+')

def remove_space(value:str):
    return regex_space.sub(' ', value.strip())

def get_nested_value(dic, key_path, default=None):
    keys = key_path.split(".")
    current = dic
    for key in keys:
        current = current.get(key, {})
        if current == {} or current is None:
            return default
    return current

def parse_price_symbol(price_raw: str):
    price_raw = price_raw.replace(",", "")

    
    price_number_match = regx_price.search(price_raw)
    
    if price_number_match is None:
        return 0,""
    
    price_number = price_number_match.group(0)
    
    price_currency = price_raw.replace(price_number, "").replace(" ", "").replace("-", "")
    
    price_converted = float(price_number)
    if price_raw.startswith("-"):
        price_converted *= -1
    
    return price_converted, price_currency

