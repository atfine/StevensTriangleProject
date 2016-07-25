# Main file for Triangle project
equilateral = "Equilateral"
isoceles    = "Isoceles"
scalene     = "Scalene"
right       = "Right Scalene"
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

  if (a == b and b == c):
    return equilateral

  if (a == b or a == c or b == c):
    return isoceles

  side = sorted([a, b, c])
  if (side[0]**2 + side[1]**2 == side[2]**2):
    return right
  else:
    return scalene


if __name__ == '__main__':
  main()
