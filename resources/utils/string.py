import re


def is_phone_number(number: str) -> bool:
    pattern = r'[a-zA-Z]'
    
    if re.search(pattern, number):
        return False
    else:
        return True

def is_too_long(characters_number: int, string: str) -> bool:
    return len(string) > characters_number