def my_csv_parser(param_1, param_2):
    return [[a for a in df.split(param_2)] for df in param_1.split("\n") if (len(df) > 0)]

print(my_csv_parser("a,b,c,e\n1,2,3,4\n", ","))