global _start
section .text
_start:
	xor rsi, rsi
	push rsi
        lea rax, [rbp - 0xe0 + 64]
        jmp rax

        
