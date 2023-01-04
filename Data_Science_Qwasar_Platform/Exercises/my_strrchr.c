#include <string.h>
#include <stdio.h>

char* my_strrchr(char* param_1, char param_2){
        char *p = NULL;

    for(; *param_1 ; ++param_1)
    {
        if(*param_1 == param_2)
            p = (char*) param_1;
    }
    return p;

}