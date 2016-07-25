import unittest
import triangleMain
from triangleMain import classifyTriangle

equilateral = 'Equilateral'
isoceles    = 'Isoceles'
scalene     = 'Scalene'
right       = 'Right Scalene'
invalid     = 'Invalid'

# classification: equilateral, isoceles, scalene, right
# data types: integer, float
# range: negative, zero, positive
# boundary: min, max
# validation: non-numbers, invalid numbers
# argument order

class TestClassifyTriangle(unittest.TestCase):
  def test_classification(self):
    self.assertEquals(classifyTriangle(5, 5, 5), equilateral)
    self.assertEquals(classifyTriangle(1, 2, 1), isoceles)
    self.assertEquals(classifyTriangle(1, 3, 5), scalene)
    self.assertEquals(classifyTriangle(3, 4, 5), right)

  def test_data_types(self):
    self.assertEqual(classifyTriangle(3, 3, 4),       isoceles)
    self.assertEqual(classifyTriangle(4.5, 4.5, 4.5), equilateral)
    self.assertEqual(classifyTriangle(3, 6, 4.5),     scalene)
    self.assertEqual(classifyTriangle(6, 8, 10.0),    right)

  def test_range(self):
    self.assertEqual(classifyTriangle(0, 1, 2),                   invalid)
    self.assertEqual(classifyTriangle(1, 2, -3),                  invalid)
    self.assertEqual(classifyTriangle(0.0001, 0.00001, 0.000001), scalene)
    self.assertEqual(classifyTriangle(10, 999999, 999999),        isoceles)
    self.assertEqual(classifyTriangle(3000000, 4000000, 5000000), right)

  def test_order(self):
    self.assertEqual(classifyTriangle(3, 4, 5), right)
    self.assertEqual(classifyTriangle(3, 5, 4), right)
    self.assertEqual(classifyTriangle(4, 3, 5), right)
    self.assertEqual(classifyTriangle(4, 5, 3), right)
    self.assertEqual(classifyTriangle(5, 3, 4), right)
    self.assertEqual(classifyTriangle(5, 4, 3), right)

  def test_invalid(self):
    self.assertEqual(classifyTriangle(5, 'b', 7), invalid)

if __name__ == '__main__':
  unittest.main()
