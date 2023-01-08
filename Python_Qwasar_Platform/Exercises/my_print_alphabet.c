#include <stdio.h>
#include <ctype.h>
#include <unistd.h>


void my_print_alphabet() {
    char a;
    for (a = 'a'; a <= 'z'; a++){
        putchar(a);}
        write(1, "\n", 1);

}