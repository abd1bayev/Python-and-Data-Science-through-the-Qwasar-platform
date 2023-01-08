#include <stdio.h>
#include <ctype.h>
    int my_isalpha(char param_1){
        if (param_1 >= 'A' && param_1 <= 'Z')
        return (1);
        if (param_1 >= 'a' && param_1 <= 'z')
        return (1);
    return (0);
}