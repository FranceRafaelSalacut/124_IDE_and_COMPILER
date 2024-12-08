bits 64
default rel
section .bss
	abc resq 1
section .data
	fmt db "%d", 10, 0
	intfmt db "%d", 0
	charfmt db "%c", 0
	strfmt db "%s", 0
	d0 dq 0
	d1 dq 15
	w0 db "hi", 10, 0
	d2 dq 1
	d3 dq 1
section .text
global main
extern ExitProcess
extern scanf
extern printf
main:
	push rbp
	mov rbp, rsp
	sub rsp, 32

	mov qword [abc], 0

Loop0:

	mov rax, qword [abc]
	cmp rax, [d1]
	jl edgingSesh0
	jmp bussing0
edgingSesh0:
	lea rcx, [w0]
	xor rax, rax
	call printf

	lea rcx, [fmt]
	mov rdx, qword [abc]
	xor rax, rax
	call printf

	lea rcx, [fmt]
	mov rdx, qword [d2]
	xor rax, rax
	call printf

	mov rax, qword [abc]
	add rax, qword [d3]
	mov qword [abc], rax

	jmp Loop0

bussing0:


	xor rax, rax
	call ExitProcess
