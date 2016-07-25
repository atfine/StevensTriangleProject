# Main file for Triangle project
import unittest

isocelesType = "Isoceles"
scaleneType = "Scalene"
equilateralType = "Equilateral"

def main():
  print "Parameter a = 3"
  a = 3
  print "Parameter b = 4"
  b = 4
  print "Parameter c = 5"
  c = 5
  
  triangleType = classifyTriangle(a,b,c)
  
  if (triangleType == isocelesType):
    print "Isoceles!"
  elif (triangleType == scaleneType):
    print "Scalene!"
  elif (triangleType == equilateralType):
    print "Equilateral!"
  else:
    print "Invalid Triangle!"
  
  
def classifyTriangle(a,b,c):
  
  validTriangle = False
  #add checks for valid numeric entries, non-zero
  
  if (a == b & b == c):
    theType = equilateralType
  elif (a == b | a == c | b == c):
    theType = isocelesType
  else:
  	theType = scaleneType
  	
  return theType