
local = [1,2,3]

def do_something(l):
  l = [1,2]
  l[1] = 20
  print(l[1])

do_something(local)
print(local[1])