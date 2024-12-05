bits 64
default rel
section .bss
section .data
	fmt db "%d", 10, 0
	intfmt db "%d", 0
	charfmt db "%c", 0
	strfmt db "%s", 0
	w0 db "h", 10, 0
section .text
global main
extern ExitProcess
extern scanf
extern printf
main:
	push rbp
	mov rbp, rsp
	sub rsp, 32



	xor rax, rax
	call ExitProcess
