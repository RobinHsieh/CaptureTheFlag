int happy()
{
  puts(&byte_4034B0);
  puts(&byte_403548);
  puts(&byte_4035E0);
  puts(&byte_403678);
  puts(&byte_403710);
  puts(&byte_4037A8);
  puts(&byte_403840);
  puts(&byte_4038D8);
  puts(&byte_403970);
  puts(&byte_403A08);
  puts(&byte_403AA0);
  puts(&byte_403B38);
  puts(&byte_403BD0);
  puts(&byte_403C68);
  puts(&byte_403D00);
  puts(&byte_403D98);
  puts(&byte_403E30);
  puts(&byte_403EC8);
  puts(&byte_403F60);
  puts(&byte_403FF8);
  puts(&byte_404090);
  puts(&byte_404128);
  return puts(&byte_4041C0);
}



int heh()
{
  puts(&byte_402128);
  puts(&byte_4021F0);
  puts(&byte_4022B8);
  puts(&byte_402380);
  puts(&byte_402448);
  puts(&byte_402510);
  puts(&byte_4025D8);
  puts(&byte_4026A0);
  puts(&byte_402768);
  puts(&byte_402830);
  puts(&byte_4028F8);
  puts(&byte_4029C0);
  puts(&byte_402A88);
  puts(&byte_402B50);
  puts(&byte_402C18);
  puts(&byte_402CE0);
  puts(&byte_402DA8);
  puts(&byte_402E70);
  puts(&byte_402F38);
  puts(&byte_403000);
  puts(&byte_4030C8);
  puts(&byte_403190);
  puts(&byte_403258);
  puts(&byte_403320);
  return puts(&byte_4033E8);
}



int init()
{
  setvbuf(stdin, 0LL, 2, 0LL);
  setvbuf(stdout, 0LL, 2, 0LL);
  return setvbuf(stderr, 0LL, 2, 0LL);
}



unsigned __int64 welcome()
{
  char v1[40]; // [rsp+0h] [rbp-30h] BYREF
  unsigned __int64 v2; // [rsp+28h] [rbp-8h]

  v2 = __readfsqword(0x28u);
  puts("Anya wants to play a game with you");
  happy();
  printf("What's your name ?\nName: ");
  __isoc99_scanf("%40s", v1);
  printf("Hello %s, let's start the game!\n\n", v1);
  return v2 - __readfsqword(0x28u);
}



int wakuwaku()
{
  __int64 v1; // [rsp+10h] [rbp-10h]
  __int64 (**v2)(void); // [rsp+18h] [rbp-8h]

  rand();
  puts("I really like peanuts");
  puts("Guess how many peanuts I ate today");
  printf("Place your bets (minimum is $10000) : ");
  __isoc99_scanf("%d", v1);
  fflush(stdin);
  printf("Guess your number (ans betwwen 0~999) : ");
  __isoc99_scanf("%d", v2);
  if ( v2 != &random )
  {
    puts("Wrong anwser");
    heh();
    exit(0);
  }
  happy();
  return execve("/bin/sh", 0LL, 0LL);
}



int __fastcall main(int argc, const char **argv, const char **envp)
{
  init(argc, argv, envp);
  welcome();
  wakuwaku();
  return 0;
}
