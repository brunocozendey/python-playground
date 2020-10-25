def mdc(x,y):
  '''
  int int => int
  mdc(x,y) => z
  Find the greatest common divisor among x and y.
  '''

  a = max(abs(x),abs(y))
  b = min(abs(x),abs(y))
  if (a%b == 0):
      return b
  else:
    for i in reversed(range(-b,b)):
      if ((b%i == 0) and (a%i == 0)):
        return i
    return 1

print(mdc(35,-15))
