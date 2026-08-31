import string

DIGITS = string.ascii_lowercase

def to_base_26(num):
    if num == 0:
        return "a"

    result = []
    while num:
        num, remainder = divmod(num, 26)
        result.append(DIGITS[remainder])
    
    result.reverse()
    return "".join(result)