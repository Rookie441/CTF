#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

#define ZERO (123 == 321)


int main() {
	printf("This is me --> ");
	fflush(stdout);

	char a[10] = "hostn";
	strcat(a, "ame");
  system(a);

  system("id");

	char b[70] = "You want this power right?";
	strncat(b, "Too bad you can't :P\n", 50);

  printf("^ the all and mighty powerful user\n"); printf(b);

  printf("\n\nTalk back at me if you want :PPPP\n");
  fflush(stdout);
  char text[64];
  gets(text);

  return ZERO;
}










































































char IlikeTOnameVARIABLESlikeTHIS[] = "/bin/sh";

