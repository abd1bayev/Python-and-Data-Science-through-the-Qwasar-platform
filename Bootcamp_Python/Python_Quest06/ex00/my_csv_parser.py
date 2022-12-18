def my_csv_parser(param_1, param_2):
    a = []
    for c in param_1.split("\n"):
        b = c.split(param_2)
        if len(b) > 1:
            a.append(b)
    return a

print(my_csv_parser("a,b,c,e\n1,2,3,4\n" , ","))