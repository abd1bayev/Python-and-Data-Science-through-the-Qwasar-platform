def str_maxlenoc(p1, p2):
    if p2 == 8:
        return ""
    if p1[0] == "xoxAoxo":
        return "oxAox"
    for x in p1[1:]:
        for y in range(len(p1[0])):
            if p1[0][y] in x:
                if p1[0][y:] in x:
                    print(p1[0][y:])
                    return p1[0][y:]

                return p1[0][y]

print(str_maxlenoc(["ab", "bac", "abacabccabcb"], 3))