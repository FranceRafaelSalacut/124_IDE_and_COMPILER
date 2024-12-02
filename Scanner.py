from Terminals import Terminal as T
import compiler.code_generator as generator
import re
import os

D_TYPE = ['int']
K_WORD = ['rizz', 'skibidi', 'galvanized', 'fanumTax', 'alpha', 'beta', 'sigma']
PUNCTUATOR = ['(', ')', ";", '"', ':']
OPERATOR = ['=', '-', "+", "*", "/", "==", ">=", "<=", "<", ">"]

table = [
[1,	2,	6,	4,	6,	1,	1,	1,	6, 4, 4],
[0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
[6,	3,	2,	6,	6,	6,	6,	6,	6, 6, 6],
[0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
[6,	6,	6,	6,	5,	6,	6,	6,	6, 6, 6],
[0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
[0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
]

def manual_tokenize_(str):
    tokens = []
    delimiter = [',', ';', ' ', "==", "=", ".", "(", ")", '"', "+", "-", "*", "/", "<", ">", ":"]

    pattern = f"({'|'.join(map(re.escape, delimiter))})"

    # Split the string and include the delimiters
    result = re.split(pattern, str)

    # Remove empty strings from the result
    tokens = list(filter(None, result))

    temp = []
    literalCheck = False
    literal = ""

    for tok in tokens:
        if tok == '\"':
            literalCheck = not literalCheck
            if not literalCheck:
                temp.append(literal)
                literal = ''
            temp.append('\"')
        elif literalCheck:
            literal += tok
        elif tok != " " and tok != "\n":
            temp.append(tok)
        
    tokens = temp

    print("tokens", tokens)
    return tokens

def classify(token):
    if token == "alpha":
        return 9
    elif token == "beta":
        return 10
    elif token in K_WORD:
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

def Tokenize(token, symbolTable, literalTable):
    terminal = T(token, symbolTable, literalTable)
    return (classify2(token), terminal)

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
    symbolTable = {}
    literalTable = {'d': 0, 'w' : 0}

    for tok in Token:
        state = table[state][classify(tok)]

        if classify2(tok) == "Literal":
            literal+=1
        else:
            literal=0

        if expect_identifier:
            Tokenized.append(Tokenize([tok], symbolTable, literalTable))
            expect_identifier = False
        else:
            if literal <= 1:
                Tokenized.append(Tokenize(tok, symbolTable, literalTable))
            

        if state == 1 or state == 3 or state == 5 or state == 6:
            state = 0

        if state == 4:
            expect_identifier = True

    return Tokenized, symbolTable, literalTable

with open('Test_case/ScannerTest.txt', 'r') as file:
    generate = True
    for line in file:
        print(line, end="")
        tokens, symbols, literals = Scanner(line)
        if generate:
            asm = generator.CodeGenerator(tokens, symbols, literals, None)
            asm.generateMachineCode()
            generate = False
        print(tokens, end="\n\n")
        print(symbols)
        print(literals)

