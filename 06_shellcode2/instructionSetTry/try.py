from pwn import *
context.arch='amd64'
for i in range(0x100):
    print(disasm(b"\x0c\x87\x63" + bytes([i])))
    print()

