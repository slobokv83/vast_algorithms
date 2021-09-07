"""
aabbccsjdalsakfjtt
"""

def char_app(input, appearance):
  dict_char = {}
  for i in input:
    if i not in dict_char:
      dict_char[i] = 1
    else:
      dict_char[i] += 1

  for key, value in dict_char.items():
    if value == appearance:
      return key

    # if dict_char[i] == appearance:
    #   return i

print(char_app('bbcccsjdalsakfjtt', 2))