def my_split(param_1, param_2):
 if len(param_1) == 0 and len(param_2)==0:
  return []
 return param_1.split(param_2)

print(my_split("abc def gh-!", "-"))