def number_of_digit_one(param_1):
    countr = 0;
    for i in range(1, param_1 + 1):
        str1 = str(i);
        countr += str1.count("1");

    return countr;

print(number_of_digit_one(13))