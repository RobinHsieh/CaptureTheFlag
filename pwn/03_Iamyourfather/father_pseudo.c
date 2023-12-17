__int64 init_0()
{
  setvbuf(stdout, 0LL, 2LL, 0LL);
  setvbuf(stdin, 0LL, 2LL, 0LL);
  return setvbuf(stderr, 0LL, 2LL, 0LL);
}



__int64 banner()
{
  puts("1. create a child");
  puts("2. show how many children we created");
  return puts("3. stop create child and get out");
}



int __fastcall main(int argc, const char **argv, const char **envp)
{
  int v3; // edx
  int v4; // ecx
  int v5; // r8d
  int v6; // r9d
  int v7; // edx
  int v8; // ecx
  int v9; // r8d
  int v10; // r9d
  int v11; // eax
  int v12; // edx
  int v13; // ecx
  int v14; // r8d
  int v15; // r9d
  char v17; // [rsp+0h] [rbp-30h]
  int v18; // [rsp+4h] [rbp-2Ch] BYREF
  int v19; // [rsp+8h] [rbp-28h]
  int v20; // [rsp+Ch] [rbp-24h]
  char buf[8]; // [rsp+10h] [rbp-20h] BYREF
  __int64 v22; // [rsp+18h] [rbp-18h]
  unsigned __int64 v23; // [rsp+28h] [rbp-8h]

  v23 = __readfsqword(0x28u);
  *(_QWORD *)buf = 0LL;
  v22 = 0LL;
  v19 = 0;
  init_0(argc, argv, envp);
  while ( 1 )
  {
    while ( 1 )
    {
      banner();
      _isoc99_scanf((unsigned int)"%d", (unsigned int)&v18, v3, v4, v5, v6, v17);
      if ( v18 != 1 )
        break;
      v20 = fork();
      ++v19;
      if ( v20 == -1 )
      {
        perror("fork");
        exit(1LL);
      }
      if ( !v20 )
      {
        v11 = getpid();
        printf((unsigned int)"I'm child, my id is %d\n", v11, v12, v13, v14, v15, v17);
        puts("Say something to your father");
        read(0, buf, 0x100uLL);
        return 0;
      }
      wait(0LL);
    }
    if ( v18 != 2 )
      break;
    printf((unsigned int)"we create %d children !!!\n", v19, v7, v8, v9, v10, v17);
  }
  puts("Please help me find my children !!!!!");
  read(0, buf, 0x100uLL);
  return 0;
}
