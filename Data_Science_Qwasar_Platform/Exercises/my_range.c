int* my_range(int param_1, int param_2)
{
    int* range = malloc(sizeof(int)*(param_2-param_1));
    for (int i = 0; i < param_2 - param_1; i++){
        range[i] = param_1 + i;
    }
    return range;
}