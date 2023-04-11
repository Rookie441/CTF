#include <unistd.h>
#include <string.h>
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <signal.h>

#define MAX_TITLE_LENGTH 10
#define IS_DEBUG 0

char *filename = "fst_secrets.txt";
int permission = IS_DEBUG;

void setup();
void filegone();

void print_whole_file(FILE *fptr) {
    char c;
    while ((c = fgetc(fptr)) != EOF) {
        printf("%c", c);
    }
}

// Check all titles collected
void check_log() {
    FILE *fp;
    fp = fopen(filename, "r");

    if (fp == NULL)
        filegone();

    print_whole_file(fp);

    fclose(fp);
}

// SUPER SAFE method to read string from user
char *get_user_input() {
    char *buf = malloc(MAX_TITLE_LENGTH + 1);
    fgets(buf, MAX_TITLE_LENGTH, stdin);
    fflush(stdin);
    buf[MAX_TITLE_LENGTH] = 0;    // Null terminate
    return buf;
}

void get_title() {
    int *perm = &permission;
    FILE *fp;
    fp = fopen(filename, "a");    // Open my file of secrets

    if (fp == NULL)
        filegone();

    char *input;
    input = get_user_input();     // Get user input safely

    char result[64] = "";
    char prefix_format[8] = "%s";
    char prefix[8] = "--> ";

    strcat(result, prefix_format);
    strcat(result, input);

    fprintf(fp, result, prefix);
    fclose(fp);

    if (*perm)
        check_log();
}

int main() {
    setup();

    printf("Format String Theory is going to be the next big hit!\n");
    printf("Can you help me with the title of my papers? I need quite a few...\n\n");

    int permission = IS_DEBUG;

    while(1)
        get_title();

    return 0;
}

void filegone() {
    printf("File is gone?!?!?!\n");
    exit(1);
}

void timeout() {
    printf("Time's up :(\n");
    exit(0);
}

void setup() {
    setvbuf(stdin,  NULL, _IONBF, 0);   // Switch off I/O buffering
    setvbuf(stdout, NULL, _IONBF, 0);   // Switch off I/O buffering
    setvbuf(stderr, NULL, _IONBF, 0);   // Switch off I/O buffering

    signal(SIGALRM, timeout);           // Set program to exit on timeout
    alarm(30);                          // Exit program after 30s
}

