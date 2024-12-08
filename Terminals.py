
PUNCTUATOR = ['(', ')', ";", '"', ':']
OPERATOR = ['=', '-', "+", "*", "/", "==", "<=", ">=", "<", ">", "!="]

def Terminal(token, symbols, literals):
    if type(token) == list:
        symbols[token[0]] = symbols["var"]
        return token[0]
    elif token in symbols.keys():
        return token        
    elif token == "rizz":
        return "r"
    elif token == "skibidi":
        return "b"
    elif token == "fanumTax":
        return "f"
    elif token == "galvanized":
        return "g"
    elif token == "alpha":
        return "h"
    elif token == "beta":
        return "e"
    elif token == "sigma":
        return "m"
    elif token == "goon":
        return "n"
    elif token == "edge":
        return "ed"
    elif token == "buss":
        return "buss"
    elif token == "blow":
        return "blow"
    elif token in ('int', 'char'):
        symbols["var"] = token
        return token
    elif token in PUNCTUATOR or token in OPERATOR:
        return token
    elif token.isdigit():
        id = literals['d']
        literals['d'] = literals['d'] + 1
        key = f'd{id}'
        literals[key] = token
        return key
    elif type(token) == str:
        id = literals['w']
        literals['w'] = literals['w'] + 1
        key = f'w{id}'
        literals[key] = token
        return key
    else:
        return "Unidentified"
        