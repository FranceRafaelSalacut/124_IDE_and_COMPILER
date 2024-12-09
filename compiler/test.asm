bits 64
default rel
section .bss
	num resq 1
section .data
	fmt db "%d", 10, 0
	intfmt db "%d", 0
	charfmt db "%c", 0
	strfmt db "%s", 0
	d0 dq 12
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


	xor rax, rax
	call ExitProcess
