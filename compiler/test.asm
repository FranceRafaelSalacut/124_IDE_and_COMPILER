bits 64
default rel
section .bss
	num resq 1
section .data
	fmt db "%d", 10, 0
	intfmt db "%d", 0
	charfmt db "%c", 0
	strfmt db "%s", 0
	d0 dq 0
	d1 dq 25
	d2 dq 1
section .text
global main
extern ExitProcess
extern scanf
extern printf
main:
	push rbp
	mov rbp, rsp
	sub rsp, 32

	mov qword [num], 0

Loop0:

	mov rax, qword [num]
	cmp rax, [d1]
	jle edgingSesh0
	jmp bussing0
edgingSesh0:
	lea rcx, [fmt]
	mov rdx, qword [num]
	xor rax, rax
	call printf

	mov rax, qword [num]
	sub rax, qword [d2]
	mov qword [num], rax

	jmp Loop0

bussing0:


	xor rax, rax
	call ExitProcess
