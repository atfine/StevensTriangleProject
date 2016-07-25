# Main file for Triangle project
import unittest

isocelesType = "Isoceles"
scaleneType = "Scalene"
equilateralType = "Equilateral"

def main:
  print "Parameter a = 3"
  a = 5
  print "Parameter b = 4"
  b = 4
  print "Parameter c = 5"
  c = 5
  
  triangleType = classifyTriangle(a,b,c)
  
  
  
def classifyTriangle(a,b,c):
  
  validTriangle = False
  
  if (a == b & b == c):
    theType = equilateralType
  elif (a == b | a == c | b == c)
    theType = isocelesType
  else:
  	theType = scaleneType

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(classifyTriangle(3,3,4), 4)