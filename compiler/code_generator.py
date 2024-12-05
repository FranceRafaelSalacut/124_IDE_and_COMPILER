import os
import subprocess

class CodeGenerator:
    def __init__(self, tokens, symbols, literals, filepath):
        self.tokens = tokens
        self.symbolTable = symbols
        self.literalTable = literals
        self.filepath = filepath
        del self.literalTable['w']
        del self.literalTable['d']
        del self.symbolTable['var']

    def generateMachineCode(self):
        jumps = {"==": "je", "!=": "jne", "<": "jl", ">": "jg", "<=": "jle", ">=": "jge"}
        conditional = ""
        nthConditional = -1
        nthLoop = -1
        asm = open('compiler/test.asm', 'w')
        asm.write('bits 64\n')
        asm.write("default rel\n")
        asm.write('section .bss\n')
        for key, value in self.symbolTable.items():
            asm.write(f'\t{key} {"resq" if value == "int" else "resb"} 1\n' )
        asm.write('section .data\n')
        asm.write('\tfmt db \"%d\", 10, 0\n')
        asm.write('\tintfmt db \"%d\", 0\n')
        asm.write('\tcharfmt db \"%c\", 0\n')
        asm.write('\tstrfmt db \"%s\", 0\n')
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
                fmt = self.tokens[i-1][1] + 'fmt'
                asm.write(f'\tlea rcx, {fmt}\n')
                asm.write(f'\tlea rdx, [{self.tokens[i][1]}]\n')
                asm.write('\txor rax, rax\n')
                asm.write('\tcall scanf\n')
            elif self.tokens[i][1] == 'f':          # fanumTax operation
                if self.tokens[i+2][0] == 'Constant':
                    constant1 = self.tokens[i+2][1]
                    op = self.tokens[i+3][1]
                    i += 4  
                else:
                    constant1 = self.tokens[i+3][1]
                    op = self.tokens[i+4][1]
                    i += 5  
                
                if self.tokens[i][0] == 'Constant':
                    constant2 = self.tokens[i][1]
                    i += 2
                else:
                    constant2 = self.tokens[i+1][1]
                    i += 3

                
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

            elif self.tokens[i][1] == "h":      # alpha (if)
                nthConditional += 1
                nthBeta = -1
                conditional = "alpha"
                asm.write(f'\tmov rax, qword [{self.tokens[i+1][1]}]\n')
                asm.write(f'\tcmp rax, {self.literalTable[self.tokens[i+3][1]]}\n')
                asm.write(f'\t{jumps[self.tokens[i+2][1]]} inalpha{nthConditional}\n')
                asm.write(f'\tjmp endalpha{nthConditional}\n\n')
                asm.write(f'inalpha{nthConditional}:\n\n')
                i += 5
            elif self.tokens[i][1] == "e":      # beta (else if)
                asm.write(f'\n\tjmp goon{nthConditional}\n\n')
                if conditional == "alpha":
                    asm.write(f'endalpha{nthConditional}:\n')
                else:
                    asm.write(f'endbeta{nthBeta}{nthConditional}:\n')
                nthBeta += 1
                conditional = "beta"
                asm.write(f'\tmov rax, qword [{self.tokens[i+1][1]}]\n')
                asm.write(f'\tcmp rax, {self.literalTable[self.tokens[i+3][1]]}\n')
                asm.write(f'\t{jumps[self.tokens[i+2][1]]} inbeta{nthBeta}{nthConditional}\n')
                asm.write(f'\tjmp endbeta{nthBeta}{nthConditional}\n\n')
                asm.write(f'inbeta{nthBeta}{nthConditional}:\n\n')
                i += 5
            
            elif self.tokens[i][1] == 'm':      # sigma (else)
                asm.write(f'\n\tjmp goon{nthConditional}\n\n')
                if conditional == "alpha":
                    asm.write(f'endalpha{nthConditional}:\n')
                else:
                    asm.write(f'endbeta{nthBeta}{nthConditional}:\n')
                conditional = ""
                i += 2

            elif self.tokens[i][1] == 'n':       # goon (end if)
                if conditional == "alpha":
                    asm.write(f'\n\tjmp goon{nthConditional}\n\n')
                    asm.write(f'endalpha{nthConditional}:\n')
                elif conditional == 'beta':
                    asm.write(f'\n\tjmp goon{nthConditional}\n\n')
                    asm.write(f'endbeta{nthBeta}{nthConditional}:\n')
                asm.write(f'goon{nthConditional}:\n\n')
                i += 2

            elif self.tokens[i][1] == 'ed':
                nthLoop += 1
                asm.write(f'Loop{nthLoop}:\n\n')
                i += 1
                if self.tokens[i][0] == "Constant":
                    LHS = self.tokens[i][1]
                    operation = self.tokens[i+1][1]
                    i += 2
                else:
                    LHS = self.tokens[i+1][1]
                    operation = self.tokens[i+2][1]
                    i += 3
                
                if self.tokens[i][0] == "Constant":
                    RHS = self.tokens[i][1]
                    i += 2
                else:
                    RHS = self.tokens[i+1][1]
                    i += 3
                
                asm.write(f'\tmov rax, qword [{LHS}]\n')
                asm.write(f'\tcmp rax, [{RHS}]\n')
                asm.write(f'\t{jumps[operation]} edgingSesh{nthLoop}\n')
                asm.write(f'\tjmp bussing{nthLoop}\n')
                asm.write(f'edgingSesh{nthLoop}:\n')

            elif self.tokens[i][1] == "buss":           # end loop
                asm.write(f'\tjmp Loop{nthLoop}\n\n')
                asm.write(f'bussing{nthLoop}:\n\n')
                i += 2
                
            else:
                i+=1
                asm.write('\n')
            
        asm.write('\n\txor rax, rax\n')
        asm.write('\tcall ExitProcess\n')
        asm.close()
    
    def compile(self):
        print("[CMD] Assembling")
        self.generateMachineCode()
        os.system(f"nasm -f elf64 compiler/test.asm")
        # os.remove("compiler/test.asm")
        print("[CMD] Linking")
        os.system(f"gcc -o compiler/test.exe compiler/test.o")
        os.remove("compiler/test.o")
    
    def run(self):
        print("[CMD] Running")
        subprocess.run("compiler/test.exe")