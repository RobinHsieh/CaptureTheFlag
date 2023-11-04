global _start
section .text
_start:
        or     al, 0x87
;        movsxd edx, eax  ; this line can be executed, but it can't be assembled by nasm
        mov ebx, ebx
