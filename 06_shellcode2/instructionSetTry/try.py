from pwn import *
context.update(arch='amd64', os='linux')
print(disasm(b"\x0c\x87\x63"))
for i in range(0x100):
    print(disasm(b"\x0c\x87\x63" + bytes([i])))
    print()

