import os

class CodeGenerator:
    def __init__(self, tokens, symbols, literals, filepath):
        self.tokens = tokens
        self.symbolTable = symbols
        self.literalTable = literals
        self.filepath = filepath
        del self.literalTable['w']
        del self.literalTable['d']

    def generateMachineCode(self):
        asm = open('compiler/test.asm', 'w')
        asm.write('bits 64\n')
        asm.write("default rel\n")
        asm.write('section .data\n')
        asm.write('\tfmt db \"%d\", 10, 0\n')
        asm.write('\tscanfmt db \"%d\", 0\n')
        for key in self.symbolTable.keys():
            asm.write(f'\t{key} dq 0\n' )
        for key, value in self.literalTable.items():
            if key.startswith('w'):
                if '\\x' in value:
                    value = value.replace('\\x', '')
                    asm.write(f'\t{key} db \"{value}\", 0\n')
                else:
                    asm.write(f'\t{key} db \"{value}\", 10, 0\n')
            elif key.startswith('d'):
                asm.write(f'\t{key} dq {value}\n')

        asm.write('section .text\n')
        asm.write('global main\n')
        asm.write('extern ExitProcess\n')
        asm.write('extern scanf\n')
        asm.write('extern printf\n')
        asm.write('main:\n')
        asm.write("\tpush rbp\n")
        asm.write("\tmov rbp, rsp\n")
        asm.write("\tsub rsp, 32\n\n")

        i = 0
        variableStore = ""
        while i < len(self.tokens):
            if self.tokens[i][1] == 'r':            # rizz (print)
                i += 1
                if self.tokens[i+1][0] == 'Literal':
                    i+=1
                    asm.write(f'\tlea rcx, [{self.tokens[i][1]}]\n')
                    asm.write('\txor rax, rax\n')
                    asm.write('\tcall printf\n')
                    i+= 2
                else:
                    asm.write(f'\tlea rcx, [fmt]\n')
                    if self.tokens[i][0] != 'Constant':
                        i+=1
                    asm.write(f'\tmov rdx, qword [{self.tokens[i][1]}]\n')
                    asm.write('\txor rax, rax\n')
                    asm.write('\tcall printf\n')
                    i += 1
            elif self.tokens[i][1] == 'b':          # skibidi input
                i += 2
                asm.write('\tlea rcx, [scanfmt]\n')
                asm.write(f'\tlea rdx, [{self.tokens[i][1]}]\n')
                asm.write('\txor rax, rax\n')
                asm.write('\tcall scanf\n')
            elif self.tokens[i][1] == 'f':          # fanumTax operation
                if self.tokens[i+2][0] == 'Constant':
                    constant1 = self.tokens[i+2][1]
                    op = self.tokens[i+3][1]
                    constant2 = self.tokens[i+4][1]
                    i += 6  
                else:
                    constant1 = self.tokens[i+3][1]
                    op = self.tokens[i+4][1]
                    constant2 = self.tokens[i+6][1]
                    i += 8  
                if op == '+':
                    asm.write(f'\tmov rax, qword [{constant1}]\n')
                    asm.write(f'\tadd rax, qword [{constant2}]\n')
                    # mov qword [result], rax

                elif op == '-':
                    asm.write(f'\tmov rax, qword [{constant1}]\n')
                    asm.write(f'\tsub rax, qword [{constant2}]\n')
                    # mov qword [result], rax

                elif op == '*':
                    asm.write(f'\tmov rax, qword [{constant1}]\n')
                    asm.write(f'\timul rax, qword [{constant2}]\n')
                    # mov qword [result], rax

                elif op == '/':
                    asm.write(f'\tmov rax, qword [{constant1}]\n')
                    asm.write(f'\tmov rbx, qword [{constant2}]\n')
                    asm.write(f'\tcqo\n')
                    asm.write(f'\tidiv rbx\n')             
                    # mov qword [result], rax

                if variableStore != "":
                    asm.write(f'\tmov qword [{variableStore}], rax')
                    variableStore = ""
                asm.write('\n')
            elif self.tokens[i][1] == 'g':              # galvanized declaration
                variableStore = self.tokens[i+2][1]
                i += 3
                if self.tokens[i][1] == ';':
                    variableStore = ""
                    continue
                elif self.tokens[i][1] == '=':
                    i += 1

                if self.tokens[i][1] == 'f':
                    continue
                elif self.tokens[i][0] == 'Constant':
                    asm.write(f'\tmov qword [{variableStore}], {self.literalTable[self.tokens[i][1]]}\n\n')
                    i += 2
                    variableStore = ''
                elif self.tokens[i][0] == 'Data Type':
                    asm.write(f'\tmov rax, qword [{self.tokens[i+1][1]}]\n')
                    asm.write(f'\tmov qword [{variableStore}], rax\n\n')
                    i += 3
            else:
                i+=1
                asm.write('\n')
            
        asm.write('\n\txor rax, rax\n')
        asm.write('\tcall ExitProcess\n')
        asm.close()
    


