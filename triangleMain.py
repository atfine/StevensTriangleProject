# Main file for Triangle project
import unittest

isocelesType = "Isoceles"
scaleneType = "Scalene"
equilateralType = "Equilateral"
invalidType = "Invalid"

def main():
  rawa = raw_input ("Parameter A: ")
  rawb = raw_input ("Parameter B: ")
  rawc = raw_input ("Parameter C: ")
  
  triangleType = classifyTriangle(rawa,rawb,rawc)
  
  if (triangleType == isocelesType):
    print "Isoceles!"
  elif (triangleType == scaleneType):
    print "Scalene!"
  elif (triangleType == equilateralType):
    print "Equilateral!"
  else:
    print "Invalid Triangle!"
  
  
def classifyTriangle(a,b,c):
  
  # Check for valid numeric entries
  try:
    a = float (rawa)
  except:
    a = 0.0
    
  try:
    b = float (rawb)
  except:
    b = 0.0
    
  try:
    c = float (rawc)
  except:
    c = 0.0
    
  if (a == 0.0 or b == 0.0 or c == 0.0):
    theType = invalidType
  else:
    if (a == b and b == c):
      theType = equilateralType
    elif (a == b or a == c or b == c):
      theType = isocelesType
    else:
  	  theType = scaleneType
  	
  return theType
  
  
main()