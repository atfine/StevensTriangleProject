import unittest
import math
import triangleMain
from triangleMain import classifyTriangle

equilateral    = 'Equilateral'
isoceles       = 'Isoceles'
scalene        = 'Scalene'
right_scalene  = 'Right Scalene'
right_isoceles = 'Right Isoceles'
invalid        = 'Invalid'

# classification: equilateral, isoceles, scalene, right
# data types: integer, float
# range: negative, zero, positive
# boundary: min, max
# validation: non-numbers, invalid numbers
# argument order

class TestClassifyTriangle(unittest.TestCase):
  def test_classification(self):
    self.assertEquals(classifyTriangle(5, 5, 5), equilateral)
    self.assertEquals(classifyTriangle(2, 3, 2), isoceles)
    self.assertEquals(classifyTriangle(4, 3, 6), scalene)
    self.assertEquals(classifyTriangle(3, 4, 5), right_scalene)
    self.assertEquals(classifyTriangle(1, 1, math.sqrt(2)), right_isoceles)

  def test_data_types(self):
    self.assertEqual(classifyTriangle(3, 3, 4),       isoceles)
    self.assertEqual(classifyTriangle(4.5, 4.5, 4.5), equilateral)
    self.assertEqual(classifyTriangle(3, 6, 4.5),     scalene)
    self.assertEqual(classifyTriangle(6, 8, 10.0),    right_scalene)

  def test_range(self):
    self.assertEqual(classifyTriangle(0, 1, 2),                invalid)
    self.assertEqual(classifyTriangle(1, 2, -3),               invalid)
    self.assertEqual(classifyTriangle(0.0001, 0.0002, 0.0003), scalene)
    self.assertEqual(classifyTriangle(1, 1E6, 1E6),            isoceles)
    self.assertEqual(classifyTriangle(3E15, 4E15, 5E15),       right_scalene)

  def test_order(self):
    self.assertEqual(classifyTriangle(3, 4, 5), right_scalene)
    self.assertEqual(classifyTriangle(3, 5, 4), right_scalene)
    self.assertEqual(classifyTriangle(4, 3, 5), right_scalene)
    self.assertEqual(classifyTriangle(4, 5, 3), right_scalene)
    self.assertEqual(classifyTriangle(5, 3, 4), right_scalene)
    self.assertEqual(classifyTriangle(5, 4, 3), right_scalene)

  def test_invalid(self):
    self.assertEqual(classifyTriangle(5, 'b', 7), invalid)

if __name__ == '__main__':
  unittest.main()
