def hidenp(param_1, param_2):
    if len(param_1)==0:
        return 1
    res = []
    for p1 in range(len(param_1)):
        for p2 in range(len(param_2)):
            if param_1[p1]==param_2[p2] and (param_1[p1]>='a' and param_1[p1]<='z'):
                res.append(p2)
                break
    return int(res == sorted(res))

print(hidenp("fgex.;", "tyf34gdgf;'ektufjhgdgex.;.;rtjynur6"))