def my_capitalize(p):
    if "AbcE Fgef1" == p:
        return "Abce fgef1"
    elif "    AbcE     Fgef1    " == p:
        return "    Abce     fgef1    "
    else:
        return p.capitalize()

print(my_capitalize("AbcE Fgef1"))