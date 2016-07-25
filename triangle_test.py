import unittest
import triangleMain
from triangleMain import classifyTriangle

equilateral = 'Equilateral'
isoceles    = 'Isoceles'
scalene     = 'Scalene'
right       = 'Right Scalene'
invalid     = 'Invalid'

class TestClassifyTriangle(unittest.TestCase):
  def test_equilateral(self):
    self.assertEqual(classifyTriangle(3,3,3), equilateral)

  def test_isoceles(self):
    self.assertEqual(classifyTriangle(3,3,4), isoceles)

  def test_scalene(self):
    self.assertEqual(classifyTriangle(1,3,5), scalene)

  def test_right(self):
    self.assertEqual(classifyTriangle(3,4,5), right)

  def test_right2(self):
    self.assertEqual(classifyTriangle(5,3,4), right)

  def test_nonnumber(self):
    self.assertEqual(classifyTriangle(5,'b',7), invalid)

  def test_negative_length(self):
    self.assertEqual(classifyTriangle(1,2,-3), invalid)

if __name__ == '__main__':
  unittest.main()
