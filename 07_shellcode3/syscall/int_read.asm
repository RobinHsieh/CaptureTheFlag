global _start
section .text
_start:
        mov rax, 0x3 ; number for sys_read
        mov rbx, 0x2 ; From stdin
        int 0x80
