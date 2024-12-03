
PUNCTUATOR = ['(', ')', ";", '"', ':']
OPERATOR = ['=', '-', "+", "*", "/"]

def Terminal(token):
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
        return "d"
    elif token == "int":
        return token
    elif type(token) == str:
        return "w"
    else:
        return "Unidentified"
    
    