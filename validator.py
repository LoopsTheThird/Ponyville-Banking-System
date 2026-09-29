def negative(amount):
    if amount < 0:
        return True

    return False

def special_chars(data):
    string = str(data)
    for char in string:
        if char in ["!", '"', "#", "$", "%", "&", "'", "(", ")", "*","+", ",", "-", ".", "/", ":", ";", "<", "=", ">","?", "@", "[", "\\", "]", "^", "_", "`", "{", "|","}", "~"]:
            return True

    return False

def has_a_digit(data):
    string = str(data)
    for char in data:
        if char in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return True

    return False

def is_a_digit(data):
    string = str(data)
    if string.isdigit():
        return True

    return False