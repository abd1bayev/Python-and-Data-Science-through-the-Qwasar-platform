#ifndef STRUCT_STRING_ARRAY
#define STRUCT_STRING_ARRAY
typedef struct s_string_array
{
    int size;
    char** array;
} string_array;
#endif

int my_putchar(char c) {
    return write(1, &c, 1);
}
void my_putstr(char* param_1)
{
    int i = 0;
    while(param_1[i] != 0)
    {
        my_putchar(param_1[i]);
        i++;
    }
}
void my_print_words_array(string_array* param_1)
{
    for (int i = 0; i <param_1->size; i++) {
        my_putstr(param_1->array[i]);
        my_putchar('\n');
    }
}


//Input: ["abc", "def", "gh"]
//Output: abc
//def
//gh
//
//Return Value: nil