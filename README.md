# Write-up CTF 11/2023


## objdump commands
### objdump -h `<`executable`>`
查看執行檔的 section headers
- `Size` - section 的大小
- `VMA` - section _**預定**_ 映射 (mapping) 在記憶體中的虛擬地址 (virtual memory address)


## gdb commands
[gef –– GDB Enhanced Features 安裝教學](https://hugsy.github.io/gef/install/)


### x/`<`length/format/unit`>` `<`addr`>`
`x`: 檢查記憶體中的內容。x 是 examine 的縮寫\
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
- `b` - byte (8-bits)
- `h` - halfword (16-bits)
- `w` - word (32-bits)
- `g` - giant word (64-bits)

### checksec
檢查執行檔的安全性，是否開啟了 NX, PIE, RELRO, Canary 等等的保護機制。

### info proc mappings & vmmap
查看執行檔中，sections _**最終實際**_ 映射 (mapping) 在記憶體中的虛擬地址 (virtual memory address)
- `r` - 可讀
- `w` - 可寫
- `x` - 可執行
- `p` - 私有


## ropper commands
[Ropper 安裝教學](https://shantoroy.com/security/using-ropper-to-find-address-of-gadgets/)

### source venv/bin/activate; ropper
啟動 Ropper 交互式介面

### file `<`executable`>`
讀入 ELF 執行檔

### search `<`instruction`>`
尋找 ROP gadgets

Example:\
<img src="image/ropper_search.png" width="420" height="340">


## Challenges

### 03_Iamyourfather
#### Methods
* fork() –– Multi-Process
* Canary brute forcing
* ROP gadgets



### 04_wakuwaku
#### Methods
* PLT –– Procedure Linkage Table
* GOT –– Global Offset Table



### 05_shellcode
#### Methods
* Shellcode basic

#### Solving Process
題目有給 C code，先打開來看看：
```c
#include <stdlib.h>
#include <stdio.h>

void init() {
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);
	return;
}

int main() {
	init();
	char buf[200];

	puts("Input something in this buffer!!!");
	read(0, buf, 200);

	void (*func)() = (void (*)())buf;
	(*func)();

	return 0;
}
```



### 06_shellcode2
#### Methods
* Shellcode basic
* Shellcode crafting
* jmp instruction
* `read` syscall



### 07_shellcode3
#### Methods
* Shellcode basic
* Shellcode crafting
* NOPs
* `read` syscall



