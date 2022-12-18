def my_levenshtein(string_1, string_2):
    a = 0
    if len(string_1) == len(string_2):
        for b in range(len(string_1)):
            if string_1[b] != string_2[b]:
                a +=1
        return a

    return -1


print(my_levenshtein("GGACTGA", "GGACTGA"))
print(my_levenshtein("ACCAGGG", "ACTATGG"))
print(my_levenshtein("GGACGGATTCTG", "AGG"))