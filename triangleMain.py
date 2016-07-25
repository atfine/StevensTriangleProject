# Main file for Triangle project
equilateral = "Equilateral"
isoceles    = "Isoceles"
scalene     = "Scalene"
right       = "Right "
invalid     = "Invalid"

def main():
  a = raw_input ("Parameter A: ")
  b = raw_input ("Parameter B: ")
  c = raw_input ("Parameter C: ")
  print classifyTriangle(a,b,c)


def classifyTriangle(a,b,c):
  # Check for valid numeric entries
  try:
    a = float (a)
    b = float (b)
    c = float (c)
  except:
    return invalid

  if (a <= 0 or b <= 0 or c <= 0):
    return invalid

  if (a + b <= c): return invalid
  if (a + c <= b): return invalid
  if (b + c <= a): return invalid

  rv = ''
  if   (a == b and b == c):          rv = equilateral
  elif (a == b or a == c or b == c): rv = isoceles
  else:                              rv = scalene

  if (rv != equilateral):
    side = sorted([a, b, c])
    if isclose(side[0]**2 + side[1]**2, side[2]**2):
      rv = right + rv

  return rv



def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
  return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

if __name__ == '__main__':
  main()
