class Parser:
    def __init__(self, Scanner):
        self.tokens = Scanner.tokenStream()
        self.pos = 0
        self.loop = False
        self.Scanner = Scanner
        self.keywords = {   "r": "rizz", "b": "skibidi", "f": "fanumTax", "g": "galvanized", "h": "alpha",
                            "e": "beta", "m": "sigma", "n": "goon", "ed": "edge", "buss": "buss" ,"\"": "\"",
                            ";": ";", ":": ":", "(": "(", ")": ")"
                        }
    
    def parse(self):
        try:
            self.S()
            if self.pos < len(self.tokens):
                raise SyntaxError("Unexpected token: {}".format(self.tokens[self.pos]))
            print("You passed the test")
            return 1
        except Exception as e:
            error_message = (
                f"Error occurred at line {self.Scanner.currentLine - 1} pos {self.pos}\n"
                f"{self.Scanner.code[self.Scanner.currentLine-2]}\n"
                f"{e}"
            )
            return error_message
            # print(f"Error occurred at line {self.Scanner.currentLine - 1} pos {self.pos - 1}")
            # print(f"{self.Scanner.code[self.Scanner.currentLine]}\n{e}")
            
            # return 

    def fetchTokens(self):
        tokens = self.Scanner.tokenStream()
        if not tokens:
            return

        self.tokens = tokens
        self.pos = 0

    def checkTokens(self):
        if self.pos >= len(self.tokens):
            self.fetchTokens()    

    def checkBlockStatements(self):
        if self.pos >= len(self.tokens):
            raise SyntaxError("Ermmm what the Sigma! Expected Statements in block. ")

    def S(self):
        if self.pos < len(self.tokens):
            if self.tokens[self.pos] == 'r':
                self.P()
            elif self.tokens[self.pos] == 'g':
                self.D()
            elif self.tokens[self.pos] == 'f':
                self.O()
            elif self.tokens[self.pos] == 'b':
                self.I()
            elif self.tokens[self.pos] == 'h':
                self.C()
            elif self.tokens[self.pos] == 'int':
                self.T()
            else:
                print(f"what position ? {self.pos}")
                # raise SyntaxError("Expected P, D, O, I, T, or C")
                if self.tokens[self.pos] in self.keywords.keys():
                    raise SyntaxError(f"Unexpected keyword \"{self.keywords[self.tokens[self.pos]]}\"")
                else:
                    raise SyntaxError(f"Invalid keyword \"{self.Scanner.literalTable[self.tokens[self.pos]]}\"")
        # S' -> ε (do nothing if no valid token)

    def P(self):
        self.match('r')
        self.P_prime()
        if self.loop:
            return
        self.S_prime()

    def P_prime(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == '"':
            self.match('"')
            self.match2("w")
            self.match('"')
            self.match(";")
        elif self.tokens[self.pos] == 'int':
            self.T()
            self.var()
            self.match(";")
        # ε is handled by doing nothing

    def S_prime(self):
        self.checkTokens()    
        if self.pos < len(self.tokens):
            self.S()

    def T(self):
        self.match('int')

    def I(self):
        self.match('b')
        self.T()
        self.var()
        self.match(';')
        self.S_prime()

    def O(self):
        self.match('f')
        self.match('(')
        if self.tokens[self.pos] == 'int':
            self.T()
            self.var()
            self.Op()
            self.T()
            self.var()
        else:
            self.d()
            self.Op()
            self.d()
        self.match(')')
        if self.loop:
            return
        self.S_prime()

    def Op(self):
        if self.tokens[self.pos] in {'+', '-', '*', '/'}:
            self.match(self.tokens[self.pos])
        else:
            raise SyntaxError("Expected operator")

    def D(self):
        self.match('g')
        self.T()
        self.var()
        self.A()
        self.match(";")
        if self.loop:
            return
        self.S_prime()

    def A(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == '=':
            self.match('=')
            self.A_prime()
        # ε is handled by doing nothing

    def A_prime(self):
        if self.pos < len(self.tokens):
            if self.pos < len(self.tokens) and self.tokens[self.pos] == 'f':
                self.O()
            elif self.pos < len(self.tokens) and 'd' in self.tokens[self.pos]:
                self.d()
            else:
                self.T()
                self.var()
    

    def C(self):
        self.loop = True
        self.H()
        self.checkBlockStatements()
        if self.tokens[self.pos] != 'n':
            self.H_prime()
        self.match('n')
        self.match(";")
        self.loop = False
        self.S_prime()

    def H(self):
        self.match('h')
        self.var()
        self.match('==')
        self.d()
        self.match(':')
        self.B()

    def H_prime(self):
        if self.pos < len(self.tokens):
            self.E()
            self.checkBlockStatements()
            if self.tokens[self.pos] == 'n':
                return
            self.M_prime()
        # ε is handled by doing nothing

    def E(self):
        self.match('e')
        self.var()
        self.match('==')
        self.d()
        self.match(':')
        self.B()
        self.E_prime()

    def E_prime(self):
        if self.pos < len(self.tokens):
            if self.tokens[self.pos] == 'm':
                return
            elif self.tokens[self.pos] == 'n':
                return
            else:
                self.E()
        # ε is handled by doing nothing

    def M_prime(self):
        if self.pos < len(self.tokens):
            self.M()
        # ε is handled by doing nothing

    def M(self):
        self.match('m')
        self.match(":")
        self.B()

    def B(self):
        self.B_prime()

    def B_prime(self):
        self.S()
        #self.match(';')
        self.checkTokens()
        self.F_prime()

    def F(self):
        self.S()
        self.F_prime()

    def F_prime(self):
        if self.pos < len(self.tokens):
            if self.tokens[self.pos] == 'e':
                return
            elif self.tokens[self.pos] == 'm':
                return
            elif self.tokens[self.pos] == 'n':
                return
            else:
                self.B()
        # ε is handled by doing nothing

    def match(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == token_type:
            self.pos += 1
        else:
            raise SyntaxError("Expected token: \"{}\"".format(self.keywords[token_type]))
        
    def match2(self, token_type):
        if self.pos < len(self.tokens) and token_type in self.tokens[self.pos]:
            self.pos += 1
        else:
            raise SyntaxError("Expected token: \"{}\"".format(self.keywords[token_type]))

    def var(self):
        # Assuming var is a valid identifier
        if self.pos < len(self.tokens) and not self.tokens[self.pos].isidentifier():
            raise SyntaxError(f"\"{self.tokens[self.pos]}\" is not a valid identifier.")
        
        if self.pos < len(self.tokens) and self.tokens[self.pos] in self.Scanner.symbolTable.keys():
            self.pos += 1
        else:
            raise SyntaxError(f"Expected variable. \"{self.Scanner.literalTable[self.tokens[self.pos]]}\" referenced before declared.")

    def d(self):
        # Assuming d is some valid token (could be an identifier or literal)
        if self.pos < len(self.tokens) and self.tokens[self.pos].isidentifier():
            self.pos += 1
        else:
            raise SyntaxError("Expected d")

# Example usage
if __name__ == '__main__':
    from compiler.code_generator import CodeGenerator
    from Scanner import testing as tt

    # token = []
    # for x in tt():
    #     token.append(x[1])

    #print(token)


    #print(token[185:])

    #print(len(token))
    parser = Parser(tt())
    out = parser.parse()
    if out == 1:
        # print(parser.Scanner.tokens)
        cg = CodeGenerator(parser.Scanner.tokens, parser.Scanner.symbolTable, parser.Scanner.literalTable, None)
        cg.compile()
        # cg.run()
    else:
        print(out)