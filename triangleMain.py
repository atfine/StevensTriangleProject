# Main file for Triangle project
import unittest

isocelesType = "Isoceles"
scaleneType = "Scalene"
equilateralType = "Equilateral"
invalidType = "Invalid"

def main():
	
  runTests = raw_input ("Run tests (R) or Manual (M): ")
	
  if (runTests == "M"):
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
      
  else:
    
    print "Run units tests...Chris"
  
  
def classifyTriangle(a,b,c):
  
  # Check for valid numeric entries
  try:
    a = float (a)
  except:
    a = 0.0
    
  try:
    b = float (b)
  except:
    b = 0.0
    
  try:
    c = float (c)
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
