values = {
    '0': '0',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'A': '10',
    'B': '11',
    'C': '12',
    'D': '13',
    'E': '14',
    'F': '15'
}

values_reverse = dict((v,k) for k,v in values.items())

def hex_to_dec_char(hex_char):
    try:
        return int(values[hex_char])
    except:
        return None

def dec_to_hex_char(dec_char):
    try:
        return str(values_reverse[dec_char])
    except:
        return None

def hex_to_dec_str(hex_str):
    decimal_value = 0
    power = 0
    hex_str = hex_str.upper()
    for hex_char in hex_str[::-1]:
        decimal_char = hex_to_dec_char(hex_char) * (16 ** power)
        if decimal_char is None:
            return None
        decimal_value = decimal_char + decimal_value
        power += 1
    return str(decimal_value)

def dec_to_hex_str(dec_str):
    hex_value = ""
    dec_int = int(dec_str)
    while dec_int > 0:
        mod = dec_int % 16
        hex_char = dec_to_hex_char(str(mod))
        if hex_char is None:
            return None
        hex_value = hex_char + hex_value
        dec_int = int(dec_int / 16)
    return hex_value

def hex_add(hex_str_a, hex_str_b):
    return dec_to_hex_str(int(hex_to_dec_str(hex_str_a)) + int(hex_to_dec_str(hex_str_b)))

print(hex_add("2F31AD", "96BA07")) #C5EBB4