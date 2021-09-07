from math import ceil, floor


lst = list(range(900000))

def extract_evenly(lst, extract_number):
  elem_number = len(lst)
  div = 2
  even_start = 0
  odd_start = 1
  lst_out = []
  extract_number_init = extract_number

  if elem_number/2 > extract_number:
    return lst[::2]
  else:
    while elem_number % extract_number != 0:
      if div == 2:
        lst_out = lst[even_start::div]
   
      res = elem_number/div                       
      print('res:', res)
      extract_number = extract_number - floor(res)
      if extract_number < 1:
        break       
      print('extract_number:', extract_number)
      div = ceil(elem_number / extract_number)
      if div > elem_number/2:
        break
      if div % 2 == 1:
        div = div + 1
      print('div:', div)

      if div != 2:
        lst_out += lst[odd_start::div]
        odd_start += 2

  # if extract_number_init - len(set(lst_out)) == 0:
  #   print('***:',extract_number_init - len(set(lst_out)))
  #   pass
  # else:
  #   print('***:',extract_number_init - len(set(lst_out)))
  #   extract_number = extract_number_init - len(set(lst_out))
  #   i = 0
  #   while elem_number % extract_number != 0:
  #     print('------------')
   
  #     res = elem_number/div                       
  #     print('res:', res)
  #     if i == 0:
  #       extract_number = extract_number_init - len(set(lst_out))
  #     extract_number = extract_number - floor(res)
  #     if extract_number < 1:
  #       break       
  #     print('extract_number:', extract_number)
  #     div = ceil(elem_number / extract_number)
  #     if div > elem_number/2:
  #       break
  #     if div % 2 == 1:
  #       div = div + 1
  #     print('div:', div)

  #     if div != 2:
  #       lst_out += lst[odd_start::div]
  #       odd_start += 2
      
  #     i += 1

  return sorted(set(lst_out))
  
       # set(lst[0::2] + lst[1::12] + lst[3::180]) #

print(len(extract_evenly(lst, 530000)))

