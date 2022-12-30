def count_letter(param_1):
    royxatlar = []
    new = ""
    d = {}
    para_1 = param_1.lower()
    for i in para_1:
        royxatlar.append(i)
    for s in royxatlar:
        if s.isalpha():
            d[s] = royxatlar.count(s)
    for k,v in d.items():
        w = str(v) + k
        new += w + ", "
    return new[:-2]

print(count_letter("abbcc"))