class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        self.S()
        if self.pos < len(self.tokens):
            raise SyntaxError("Unexpected token: {}".format(self.tokens[self.pos]))

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
            elif self.tokens[self.pos] == 'H':
                self.C()
            elif self.tokens[self.pos] == 'int':
                self.T()
            else:
                raise SyntaxError("Expected P, D, O, I, T, or C")
        # S' -> ε (do nothing if no valid token)

    def P(self):
        self.match('r')
        self.P_prime()
        self.S_prime()

    def P_prime(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == 'w':
            self.match('w')
        elif self.tokens[self.pos] == 'int':
            self.T()
            self.var()
        # ε is handled by doing nothing

    def S_prime(self):
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
        self.d()
        self.Op()
        self.d()
        self.match(')')
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
        self.S_prime()

    def A(self):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == '=':
            self.match('=')
            self.A_prime()
        # ε is handled by doing nothing

    def A_prime(self):
        if self.pos < len(self.tokens):
            if self.tokens[self.pos] in {'f', 'd', 'int'}:
                self.O()
            else:
                self.d()
                self.var()

    def C(self):
        self.match('H')
        self.H()
        self.H_prime()

    def H(self):
        self.match('h')
        self.match('(')
        self.var()
        self.match('==')
        self.d()
        self.match(')')
        self.B()
        self.match('g')

    def H_prime(self):
        if self.pos < len(self.tokens):
            self.E()
            self.M_prime()
        # ε is handled by doing nothing

    def E(self):
        self.match('e')
        self.match('(')
        self.var()
        self.match('==')
        self.d()
        self.match(')')
        self.B()
        self.E_prime()

    def E_prime(self):
        if self.pos < len(self.tokens):
            self.E()
        # ε is handled by doing nothing

    def M_prime(self):
        if self.pos < len(self.tokens):
            self.M()
        # ε is handled by doing nothing

    def M(self):
        self.match('m')
        self.B()

    def B(self):
        self.match('{')
        self.B_prime()
        self.match('}')

    def B_prime(self):
        self.S()
        self.match(';')
        self.F()

    def F(self):
        self.S()
        self.F_prime()

    def F_prime(self):
        if self.pos < len(self.tokens):
            self.F()
        # ε is handled by doing nothing

    def match(self, token_type):
        if self.pos < len(self.tokens) and self.tokens[self.pos] == token_type:
            self.pos += 1
        else:
            raise SyntaxError("Expected token: {}".format(token_type))

    def var(self):
        # Assuming var is a valid identifier
        if self.pos < len(self.tokens) and self.tokens[self.pos].isidentifier():
            self.pos += 1
        else:
            raise SyntaxError("Expected variable")

    def d(self):
        # Assuming d is some valid token (could be an identifier or literal)
        if self.pos < len(self.tokens) and self.tokens[self.pos].isidentifier():
            self.pos += 1
        else:
            raise SyntaxError("Expected d")

# Example usage
from Scanner import Scanner as SC
from Scanner import testing_attention_please as tt


print(tt())


#parser = Parser(tokens)
#parser.parse()