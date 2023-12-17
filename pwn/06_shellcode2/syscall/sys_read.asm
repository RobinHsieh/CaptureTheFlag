global _start
section .text
_start:
        or    al, 0x87
;        movsxd edx, eax
        sub sp, 0xfff
        lea rsi, [rsp]
        mov rdi, rax
        xor rdx, rdx
        mov dx, 0xfff; size to read
        xor rax, rax
        syscall
