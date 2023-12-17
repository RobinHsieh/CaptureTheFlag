global _start
section .text
_start:
        push rdi
        push rsp
        pop rdi
        push 59
        pop rax
        cdq
        syscall
