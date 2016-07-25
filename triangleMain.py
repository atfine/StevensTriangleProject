# Main file for Triangle project
equilateral = "Equilateral"
isoceles    = "Isoceles"
rightIsoceles    = "Right Isoceles"
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
  side = sorted([a, b, c])
  
  if (side[2] >= side[0] + side[1]):
    return invalid
  
  if (a == b or a == c or b == c):
    if isclose(side[0]**2 + side[1]**2, side[2]**2):
      return rightIsoceles
    else:
      return isoceles

  
  if isclose(side[0]**2 + side[1]**2, side[2]**2):
    return right
  else:
    return scalene


def isclose(a, b, rel_tol=1e-09, abs_tol=0.0):
  return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

if __name__ == '__main__':
  main()
