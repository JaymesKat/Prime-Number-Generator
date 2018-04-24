import unittest
from app import prime_num_generator

# Test cases: A prime number is a natural number that is only divisible by 2 and itself
# check that list of integers is returned
# check that numbers returned are prime numbers i.e. greater than 1, divisible by 1 and themselves only
class MainTest(unittest.TestCase):
    def test_prime_num_generator(self):
       self.assertEqual(type(prime_num_generator(100)), list, msg="A list must be returned")
       self.assertTrue(isinstance(prime_num_generator(100)[-1], int), msg="Error: Integers must be written")
       self.assertEqual(prime_num_generator(100)[-2]>1)

if __name__ == '__main__':
    unittest.main()