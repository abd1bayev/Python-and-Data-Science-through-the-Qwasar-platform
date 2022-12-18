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

# Instructions:

# Your function must take in 2 strings with the exact number of characters and return an integer representing the difference between them.
#
# If your parameters are not the same size then your function will return -1.
#
# If the two strings are the same size, you must then iterate through each string and determine which characters are different. Each time there is a difference, it counts as 1.