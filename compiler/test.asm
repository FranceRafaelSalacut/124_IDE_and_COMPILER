bits 64
default rel
section .bss
	operand1 dq 1
	operand2 dq 1
	num dq 1
	correct dq 1
	result dq 1
section .data
	fmt db "%d", 10, 0
	intfmt db "%d", 0
	charfmt db "%c", 0
	strfmt db "%s", 0
	w0 db "Enter a number1: ", 0
	w1 db "Enter a number2: ", 0
	w2 db "Menu", 10, 0
	w3 db "[1] Add two numbers", 10, 0
	w4 db "[2] Subtract two numbers", 10, 0
	w5 db "[3] Multiply two numbers", 10, 0
	w6 db "[4] Divide two numbers", 10, 0
	w7 db "Enter a number: ", 0
	d0 dq 1
	d1 dq 1
	w8 db "Add Two numbers", 10, 0
	w9 db "The sum is: ", 0
	d2 dq 2
	w10 db "Subtract Two numbers", 10, 0
	w11 db "The difference is: ", 0
	d3 dq 3
	w12 db "Multiply Two numbers", 10, 0
	w13 db "The product is: ", 0
	d4 dq 4
	w14 db "Divide Two numbers", 10, 0
	w15 db "The quotient is: ", 0
	w16 db "Wrong input!!!", 10, 0
	d5 dq 0
	d6 dq 1
section .text
global main
extern ExitProcess
extern scanf
extern printf
main:
	push rbp
	mov rbp, rsp
	sub rsp, 32

	lea rcx, [w0]
	xor rax, rax
	call printf

	lea rcx, intfmt
	lea rdx, [operand1]
	xor rax, rax
	call scanf


	lea rcx, [w1]
	xor rax, rax
	call printf

	lea rcx, intfmt
	lea rdx, [operand2]
	xor rax, rax
	call scanf


	lea rcx, [w2]
	xor rax, rax
	call printf

	lea rcx, [w3]
	xor rax, rax
	call printf

	lea rcx, [w4]
	xor rax, rax
	call printf

	lea rcx, [w5]
	xor rax, rax
	call printf

	lea rcx, [w6]
	xor rax, rax
	call printf

	lea rcx, [w7]
	xor rax, rax
	call printf

	lea rcx, intfmt
	lea rdx, [num]
	xor rax, rax
	call scanf


	mov qword [correct], 1

	mov rax, qword [num]
	cmp rax, 1
	jne endalpha0

	lea rcx, [w8]
	xor rax, rax
	call printf

	lea rcx, [w9]
	xor rax, rax
	call printf

	mov rax, qword [operand1]
	add rax, qword [operand2]
	mov qword [result], rax


	jmp goon0

endalpha0:
	mov rax, qword [num]
	cmp rax, 2
	jne endbeta00

	lea rcx, [w10]
	xor rax, rax
	call printf

	lea rcx, [w11]
	xor rax, rax
	call printf

	mov rax, qword [operand1]
	sub rax, qword [operand2]
	mov qword [result], rax


	jmp goon0

endbeta00:
	mov rax, qword [num]
	cmp rax, 3
	jne endbeta10

	lea rcx, [w12]
	xor rax, rax
	call printf

	lea rcx, [w13]
	xor rax, rax
	call printf

	mov rax, qword [operand1]
	imul rax, qword [operand2]
	mov qword [result], rax


	jmp goon0

endbeta10:
	mov rax, qword [num]
	cmp rax, 4
	jne endbeta20

	lea rcx, [w14]
	xor rax, rax
	call printf

	lea rcx, [w15]
	xor rax, rax
	call printf

	mov rax, qword [operand1]
	mov rbx, qword [operand2]
	cqo
	idiv rbx
	mov qword [result], rax


	jmp goon0

endbeta20:
	lea rcx, [w16]
	xor rax, rax
	call printf

	mov qword [correct], 0

goon0:

	mov rax, qword [correct]
	cmp rax, 1
	jne endalpha1

	lea rcx, [fmt]
	mov rdx, qword [result]
	xor rax, rax
	call printf


	jmp goon1

endalpha1:
goon1:


	xor rax, rax
	call ExitProcess
