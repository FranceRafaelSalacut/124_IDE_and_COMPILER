from Terminals import Terminal as T
import compiler.code_generator as generator
import re
import os

class Scanner:
    def __init__(self, code):
        self.symbolTable = {"var": "None"}
        self.literalTable = {'d': 0, 'w' : 0}
        self.tokens = []
        self.currentLine = 1
        self.code = code

        self.D_TYPE = ['int', 'char', 'string']
        self.K_WORD = ['rizz', 'skibidi', 'galvanized', 'fanumTax', 'alpha', 'beta', 'sigma', 'goon', 'edge', 'blow', 'buss']
        self.PUNCTUATOR = ['(', ')', ";", '"', ':']
        self.OPERATOR = ['=', '-', "+", "*", "/", "==", ">=", "<=", "<", ">"]

        self.table = [
        [1,	2,	6,	4,	6,	1,	1,	1,	6, 4, 4],
        [0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
        [6,	3,	2,	6,	6,	6,	6,	6,	6, 6, 6],
        [0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
        [6,	6,	6,	6,	5,	6,	6,	6,	6, 6, 6],
        [0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
        [0,	0,	0,	0,	0,	0,	0,	0,	0, 0, 0],
        ]

    def manual_tokenize_(self, str):
        tokens = []
        delimiter = [',', ';', ' ', "==", "=", ".", "(", ")", '"', "+", "-", "*", "/", "<=", ">=" ,"<", ">", ":"]

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

        # print("tokens", tokens)
        return tokens

    def classify(self, token):
        if token == "alpha":
            return 9
        elif token == "beta":
            return 10
        elif token in self.K_WORD:
            return 0
        elif token == '"':
            return 1
        elif token in self.PUNCTUATOR:
            return 7
        elif token in self.D_TYPE:
            return 3
        elif type(token) == list:
            return 4
        elif token in self.OPERATOR:
            return 5
        elif token.isdigit():
            return 6
        elif type(token) == str:
            return 2
        else:
            return 8
        
    def classify2(self, token):
        if token in self.K_WORD:
            return "Keyword"
        elif token in self.PUNCTUATOR:
            return "Punctuator"
        elif token in self.D_TYPE:
            return "Data Type"
        elif type(token) == list:
            return "Identifier"
        elif token in self.OPERATOR:
            return "Operataor"
        elif token.isdigit():
            return "Constant"
        elif token in self.symbolTable.keys():
            return "Identifier"
        elif type(token) == str:
            return "Literal"
        else:
            return "Unidentified"

    def Tokenize(self, token):
        terminal = T(token, self.symbolTable, self.literalTable)
        return (self.classify2(token), terminal)

    def Test_Print(token):
        for tok in token:
            print(tok, end = ")(")
        print()

    def Scanner(self, line): 
        Token = self.manual_tokenize_(line)
        Tokenized = []
        state = 0
        literal = 0
        expect_identifier = False
        cond = False

        for tok in Token:
            state = self.table[state][self.classify(tok)]
            if self.classify2(tok) == "Literal":
                literal+=1
            else:
                literal=0
            
            if tok in ('alpha', 'beta'):
                cond = True

            if expect_identifier:
                Tokenized.append(self.Tokenize([tok]))
                expect_identifier = False
            else:
                if literal <= 1:
                    Tokenized.append(self.Tokenize(tok))
                

            if state == 1 or state == 3 or state == 5 or state == 6:
                state = 0

            if state == 4 and not cond:
                expect_identifier = True

        return Tokenized

    def tokenStream(self):
        while self.currentLine < len(self.code) and len(self.code[self.currentLine- 1]) == 0:
            self.currentLine += 1

        if self.currentLine-1 > len(self.code) - 1:
            return None
        

        tokens = self.Scanner(self.code[self.currentLine-1])
        self.tokens.extend(tokens)
        print(list(map(lambda x: x[1], tokens)))

        self.currentLine += 1
        return list(map(lambda x: x[1], tokens))


if __name__ == "__main__":
    with open('Test_case/CodeTest.txt', 'r') as file:
            
            # print(file.read().split('\n'))
            # for i in file.readlines().join().split('\n'):
            #     print(i)
            content = ""
            for line in file:
                content += line.strip('\n')    
                
            sc = Scanner(content)
            print(sc.tokenStream())

def testing():
    with open('Test_case/CodeTest.txt', 'r') as file:
    
        content = file.read().split('\n')
        print(content)
        sc = Scanner(content)
        print(sc.code)
        return sc
