bits 64
default rel
section .data
	fmt db "%d", 10, 0
	scanfmt db "%d", 0
	num1 dq 0
	num2 dq 0
	result dq 0
	w0 db "Enter number 1 ", 0
	w1 db "Enter number 2 ", 0
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

	lea rcx, [scanfmt]
	lea rdx, [num1]
	xor rax, rax
	call scanf


	lea rcx, [w1]
	xor rax, rax
	call printf

	lea rcx, [scanfmt]
	lea rdx, [num2]
	xor rax, rax
	call scanf


	mov rax, qword [num1]
	add rax, qword [num2]
	mov qword [result], rax

	lea rcx, [fmt]
	mov rdx, qword [result]
	xor rax, rax
	call printf


	xor rax, rax
	call ExitProcess