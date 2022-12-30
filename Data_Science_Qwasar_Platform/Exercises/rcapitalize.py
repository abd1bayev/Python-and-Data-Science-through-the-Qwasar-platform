def rcapitalize(param_1):
    res1 = param_1.split(" ")
    res2 = [x.lower() for x in res1]
    res3 = []
    for x in res2:
        if x.isalpha():
            if len(x) < 2:
                res3.append(x.upper())
            else:
                res3.append(str(x[:-1] + x[len(x)-1].upper()))
        else:
            res3.append(x)
    return " ".join(res3)


print(rcapitalize("SecONd teST A LITtle BiT   Moar comPLEX"))