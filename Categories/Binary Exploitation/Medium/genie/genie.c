#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct magicPouch {
    unsigned char guesses[48];
    void (*release)();
};

void askGenie(struct magicPouch * mp, unsigned int number) {
    printf("Genie grants you %d guesses\n", number);

    for (int i = 0; i < number; i++) {
        printf("What is your guess? ");
        unsigned int guess;
        scanf("%d", &guess);
        printf("Guess %d: %d\n", i + 1, guess);
	if (guess == 0) {
	    break;
        }

        mp->guesses[i] = guess & 0x000000ff;
    }
}


void genie_escape() {
    time_t rawtime;
    struct tm * timeinfo;
    time ( &rawtime );
    timeinfo = localtime ( &rawtime );
    
    puts("\n\nThere is magic all");
    puts("around, everywhere, if we");
    puts("have eyes to see it.");

    printf("The Genie flees in your suspicious attempts to locate her on %s.", asctime (timeinfo));
}


__asm__("nop");

void execute_genie() {
    puts("Hues bowed to the sky.");
    puts("Alluring thousands of eyes.");
    puts("A magical dyes.");
    system("cat /home/genie/flag.txt");
}

int main() {
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    struct magicPouch * little_magicPouch = malloc(sizeof(struct magicPouch));
    memset(little_magicPouch -> guesses, 0, 48);
    little_magicPouch -> release = &genie_escape;

    puts("Gathering rain clouds.");
    puts("Make way this magical night.");
    puts("For smiling full moon\n");

    int number;
    printf("Force is strong all around forty-eight; how many guesses would you like to make? ");
    scanf("%d", &number);

    if (number > 48) {
        puts("You ask Genie for the impossible.\n");
        number = 0;
    } else {
        askGenie(little_magicPouch, number);
    }

    for (int i = 0; i < number; i++) {
        puts("");
	printf("%d. ", i + 1);
        for (int j = 0; j < little_magicPouch -> guesses[i]; j++) {
            printf("*");
        }
    }

    if ((void *)*little_magicPouch -> release >= (void *)&execute_genie) {
	return 0;
    }

    if (number != 0) {
    	little_magicPouch -> release();
    }

    free(little_magicPouch);
}

