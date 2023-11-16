# Write-up CTF 11/2023

## gdb commands
### x/<length/format/unit> <addr>
#### `x`: 檢查記憶體中的內容。x 是 examine 的縮寫
length, format, unit 是可選的參數
#### length —— 顯示的單位數量
#### format —— 顯示格式
- `x` - hexadecimal (十六進制)
- `d` - decimal (十進制)
- `u` - unsigned decimal (無符號十進制)
- `o` - octal (八進制)
- `t` - binary (二進制)
- `a` - addr (地址)
- `i` - instruction (機器指令)
- `c` - char (字符)
- `s` - string (字串)
#### unit —— 顯示單位
- `b` - byte (8-bit)
- `h` - halfword (16-bit)
- `w` - word (32-bit)
- `g` - giant word (64-bit)





## 03_Iamyourfather
### Methods
* fork() –– Multi-Process
* Canary brute forcing
* ROP gadgets



## 04_wakuwaku
### Methods
* PLT –– Procedure Linkage Table
* GOT –– Global Offset Table



## 05_shellcode
### Methods
* Shellcode basic



## 06_shellcode2
### Methods
* Shellcode basic
* Shellcode crafting
* jmp instruction
* `read` syscall



## 07_shellcode3
### Methods
* Shellcode basic
* Shellcode crafting
* NOPs
* `read` syscall



