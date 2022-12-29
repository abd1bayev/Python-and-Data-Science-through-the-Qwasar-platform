#include <stdio.h>
#include <string.h>

#ifndef STRUCT_INTEGER_ARRAY
#define STRUCT_INTEGER_ARRAY
typedef struct s_integer_array
{
    int size;
    int* array;
} integer_array;
#endif

integer_array* my_sort(integer_array* ptr, char* ord)
{
    int i = 0;
    int j;
    int tmp;

    while (i < ptr->size-1)
    {
        j = 0;
        while (j < ptr->size-1)
        {
           	if (strcmp(ord, "asc") == 0)
            {
                if (ptr->array[j] > ptr->array[j+1])
                {
                    tmp = ptr->array[j];
                    ptr->array[j] = ptr->array[j+1];
                    ptr->array[j+1] = tmp;
                }
            }
            if (strcmp(ord, "desc") == 0)
            {
                if (ptr->array[j] < ptr->array[j+1])
                {
                    tmp = ptr->array[j];
                    ptr->array[j] = ptr->array[j+1];
                    ptr->array[j+1] = tmp;
                }
            }
            j += 1;
        }
        i += 1;
    }
    return ptr;
}