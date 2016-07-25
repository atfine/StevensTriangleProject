# Main file for Triangle project
isocelesType = "Isoceles"
scaleneType = "Scalene"
rightScalene = "Right Scalene"
equilateralType = "Equilateral"
invalidType = "Invalid"

def main():
  rawa = raw_input ("Parameter A: ")
  rawb = raw_input ("Parameter B: ")
  rawc = raw_input ("Parameter C: ")
  print classifyTriangle(rawa,rawb,rawc)


def classifyTriangle(a,b,c):
  # Check for valid numeric entries
  try:
    a = float (a)
    b = float (b)
    c = float (c)
  except:
    return invalidType

  if (a <= 0 or b <= 0 or c <= 0):
    return invalidType

  if (a == b and b == c):
    theType = equilateralType
  elif (a == b or a == c or b == c):
    theType = isocelesType
  else:
    theType = scaleneType
  
  return theType

if __name__ == '__main__':
  main()
