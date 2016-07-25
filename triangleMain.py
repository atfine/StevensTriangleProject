# Main file for Triangle project
import unittest

isocelesType = "Isoceles"
scaleneType = "Scalene"
rightScalene = "Right Scalene"
equilateralType = "Equilateral"
invalidType = "Invalid"

def main():
	
  runTests = raw_input ("Run tests (R) or Manual (M): ")
	
  if (runTests == "M"):
    rawa = raw_input ("Parameter A: ")
    rawb = raw_input ("Parameter B: ")
    rawc = raw_input ("Parameter C: ")
  
    triangleType = classifyTriangle(rawa,rawb,rawc)
    print triangleType
      
  else:
    unittest.main()
  
  
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

class TestTriangleClassifications(unittest.TestCase):
  def test_equilateral(self):
    self.assertEqual(classifyTriangle(3,3,3), equilateralType)

  def test_isoceles(self):
    self.assertEqual(classifyTriangle(3,3,4), isocelesType)

  def test_scalene(self):
    self.assertEqual(classifyTriangle(1,3,5), scaleneType)

  def test_right(self):
    self.assertEqual(classifyTriangle(3,4,5), rightScalene)

  def test_negative_length(self):
    self.assertEqual(classifyTriangle(1,2,-3), invalidType)

main()
