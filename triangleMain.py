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

class TestTriangleClassifications(unittest.TestCase):
    
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(3,3,3), equilateralType)
    
    def test_isoceles(self):
        self.assertEqual(classifyTriangle(3,3,4), isocelesType)
    
    def test_scalene(self):
        self.assertEqual(classifyTriangle(3,4,5), scaleneType)

if __name__ == '__main__':
    unittest.main()
#main()
