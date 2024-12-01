bits 64
default rel
section .data
	fmt db "%d", 10, 0
	scanfmt db "%d", 0
	d0 dq 5
	d1 dq 5
	d2 dq 5
	d3 dq 5
	d4 dq 5
	d5 dq 5
	d6 dq 5
	d7 dq 5
section .text
global main
extern ExitProcess
extern scanf
extern printf
main:
	push rbp
	mov rbp, rsp
	sub rsp, 32

	mov rax, qword [d0]
	add rax, qword [d1]

	mov rax, qword [d2]
	imul rax, qword [d3]

	mov rax, qword [d4]
	sub rax, qword [d5]

	mov rax, qword [d6]
	mov rbx, qword [d7]
	cqo
	idiv rbx


	xor rax, rax
	call ExitProcess
