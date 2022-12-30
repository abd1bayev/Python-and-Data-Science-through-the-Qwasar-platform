def is_anagram(a, b):
    if sorted(a) == sorted(b):
        return 1
    else:
        return 0


print(is_anagram("abcdef", "fabcde"))