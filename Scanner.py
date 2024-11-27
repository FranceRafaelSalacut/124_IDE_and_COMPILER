from Terminals import Terminal as T

D_TYPE = ['int']
K_WORD = ['rizz', 'skibidi', 'galvanized', 'fanumTax', 'alpha', 'beta', 'sigma']
PUNCTUATOR = ['(', ')', ";", '"', ':']
OPERATOR = ['=', '-', "+", "*", "/"]

table = [
[1,	2,	6,	4,	6,	1,	1,	1,	6,],
[0,	0,	0,	0,	0,	0,	0,	0,	0,],
[6,	3,	2,	6,	6,	6,	6,	6,	6,],
[0,	0,	0,	0,	0,	0,	0,	0,	0,],
[6,	6,	6,	6,	5,	6,	6,	6,	6,],
[0,	0,	0,	0,	0,	0,	0,	0,	0,],
[0,	0,	0,	0,	0,	0,	0,	0,	0,],
]


def manual_tokenize_(str):
    tokens = []
    delimiter = [',', ';', ' ', "=", ".", "(", ")", '"', "+", "-", "*", "/"]

    token = ''
    for char in str:
        if char in delimiter:
            if token != '':
                tokens.append(token)
            tokens.append(char)
            token = ''
        else:
            token = token + char

    tokens = [tok for tok in tokens if tok != " "]
    print(tokens)
    return tokens

def classify(token):
    if token in K_WORD:
        return 0
    elif token == '"':
        return 1
    elif token in PUNCTUATOR:
        return 7
    elif token in D_TYPE:
        return 3
    elif type(token) == list:
        return 4
    elif token in OPERATOR:
        return 5
    elif token.isdigit():
        return 6
    elif type(token) == str:
        return 2
    else:
        return 8
    
def classify2(token):
    if token in K_WORD:
        return "Keyword"
    elif token in PUNCTUATOR:
        return "Punctuator"
    elif token in D_TYPE:
        return "Data Type"
    elif type(token) == list:
        return "Identifier"
    elif token in OPERATOR:
        return "Operataor"
    elif token.isdigit():
        return "Constant"
    elif type(token) == str:
        return "Literal"
    else:
        return "Unidentified"

def Tokenize(token):
    return (classify2(token), T(token))

def Test_Print(token):
    for tok in token:
        print(tok, end = ")(")
    print()

def Scanner(line): 
    Token = manual_tokenize_(line)
    Tokenized = []
    state = 0
    literal = 0
    expect_identifier = False

    for tok in Token:
        state = table[state][classify(tok)]

        if classify2(tok) == "Literal":
            literal+=1
        else:
            literal=0

        if expect_identifier:
            Tokenized.append(Tokenize([tok]))
            expect_identifier = False
        else:
            if literal <= 1:
                Tokenized.append(Tokenize(tok))
            

        if state == 1 or state == 3 or state == 5 or state == 6:
            state = 0

        if state == 4:
            expect_identifier = True

    return Tokenized


with open('Test_case/ScannerTest.txt', 'r') as file:
    for line in file:
        print(line, end="")
        print(Scanner(line), end="\n\n")


