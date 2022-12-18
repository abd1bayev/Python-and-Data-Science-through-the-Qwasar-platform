def my_roman_numerals_converter(son):
    sonlar = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    rim_raqam = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'LC', 'C', 'CD', 'D', 'DM', 'M']
    javob = ""
    a = 12
    while son != 0:
        if sonlar[a] <= son:
            javob += rim_raqam[a]
            son = son - sonlar[a]
        else:
            a -= 1

    return javob

print(my_roman_numerals_converter(14))
print(my_roman_numerals_converter(79))
print(my_roman_numerals_converter(845))
print(my_roman_numerals_converter(2022))

# Description:

# Write a function to convert from normal numbers to Roman Numerals.
#
# The Romans wrote numbers using letters - I, V, X, L, C, D, M. (notice
# these letters have lots of straight lines and are hence easy to hack
# into stone tablets).
#
#  1  => I
# 10  => X
#  7  => VII
# There is no need to be able to convert numbers larger than about 3000.
# (The Romans themselves didn't tend to go any higher)
#
# Wikipedia says: Modern Roman numerals ... are written by expressing each
# digit separately starting with the left most digit and skipping any
# digit with a value of zero.
#
# To see this in practice, consider the example of 1990.
#
# In Roman numerals 1990 is MCMXC:
#
# 1000=M
# 900=CM
# 90=XC
#
# 2008 is written as MMVIII:
#
# 2000=MM
# 8=VIII
#
# See also: http://www.novaroma.org/via_romana/numbers.html
#
# It will return a string with the roman numeral.