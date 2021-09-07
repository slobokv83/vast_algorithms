"""
a = [-1, 15, 0, 0, 0, 0]
b = [4, 3, 2, 1]
"""
a = [-1, 15, 0, 0, 0, 0]
b = [4, 3, 2, 1]

def array_merged(a, b):
  a = a[0:len(a)- len(b)] + b
  iterations = len(a)

  def single_iteration(iterations):
    for i in range(iterations):
      if i > 0:
        if a[i-1] > a[i]:
          temp = a[i]
          a[i] = a[i-1]
          a[i-1] = temp

    return a
  
  for i in range(len(a)):
    a = single_iteration(iterations)
    iterations -= 1

  return a


print(array_merged(a, b))