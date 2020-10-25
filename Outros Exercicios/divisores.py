def divisors(a):
  '''
  int a => list
  List all divisors from a
  '''
  print(list(filter(lambda x: a%x == 0, range(1,a+1))))
divisors(7342364264762364276)
