bits 64
default rel
section .data
	fmt db "%d", 10, 0
	scanfmt db "%d", 0
	num dq 0
	w0 db "Hello World << 25 ", 0
	d0 dq 25
section .text
global main
extern ExitProcess
extern scanf
extern printf
main:
	push rbp
	mov rbp, rsp
	sub rsp, 32

	lea rcx, [scanfmt]
	lea rdx, [num]
	xor rax, rax
	call scanf


	lea rcx, [w0]
	xor rax, rax
	call printf

	lea rcx, [fmt]
	mov rdx, qword [d0]
	xor rax, rax
	call printf

	lea rcx, [fmt]
	mov rdx, qword [num]
	xor rax, rax
	call printf


	xor rax, rax
	call ExitProcess
