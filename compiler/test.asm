bits 64
default rel
section .bss
<<<<<<< HEAD
	tmp resq 1
	operand1 resq 1
	operand2 resq 1
=======
>>>>>>> c5caf0e34499ef7aaa212d1fe147a8ae323491e3
	num resq 1
section .data
	fmt db "%d", 10, 0
	mt db "", 0
	intfmt db "%d", 0
	charfmt db "%c", 0
	strfmt db "%s", 0
<<<<<<< HEAD
	endstr db "Gyatt has finished execution. Enter any number to continue.", 10, 0
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
	d7 dq 0
	d8 dq 15
	d9 dq 1
=======
	d0 dq 12
>>>>>>> c5caf0e34499ef7aaa212d1fe147a8ae323491e3
section .text
global main
extern ExitProcess
extern scanf
extern printf
main:
	push rbp
	mov rbp, rsp
	sub rsp, 32

	mov qword [num], 12

	lea rcx, [fmt]
	mov rdx, qword [num]
	xor rax, rax
	call printf


<<<<<<< HEAD
	jmp goon1

endalpha1:
goon1:

	mov qword [num], 0

Loop0:

	mov rax, qword [num]
	cmp rax, [d8]
	jl edgingSesh0
	jmp bussing0
edgingSesh0:
	lea rcx, [fmt]
	mov rdx, qword [num]
	xor rax, rax
	call printf

	mov rax, qword [num]
	add rax, qword [d9]
	mov qword [num], rax

	jmp Loop0

bussing0:

; EXIT
	lea rcx, [endstr]
	xor rax, rax
	call printf
	lea rcx, intfmt
	lea rdx, [tmp]
	xor rax, rax
	call scanf

=======
>>>>>>> c5caf0e34499ef7aaa212d1fe147a8ae323491e3
	xor rax, rax
	call ExitProcess
