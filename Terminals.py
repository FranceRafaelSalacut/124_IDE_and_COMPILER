
PUNCTUATOR = ['(', ')', ";", '"', ':']
OPERATOR = ['=', '-', "+", "*", "/"]

def Terminal(token, symbols, literals):
    if type(token) == list:
        return "var"
    elif token == "rizz":
        return "r"
    elif token == "skibidi":
        return "b"
    elif token == "fanumTax":
        return "f"
    elif token == "galvanized":
        return "g"
    elif token in PUNCTUATOR or token in OPERATOR:
        return token
    elif token.isdigit():
        id = len(symbols)
        key = f'd{id}'
        symbols[key] = token
        return key
    elif type(token) == str:
        id = len(literals)
        key = f'w{id}'
        literals[key] = token
        return key
    else:
        return "Unidentified"
    
    