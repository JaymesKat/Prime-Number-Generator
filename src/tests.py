import unittest
from app import prime_num_generator, is_prime
import random

# Test cases: A prime number is a natural number that is only divisible by 2 and itself
# check that list of integers is returned
# check that numbers returned are prime numbers i.e. greater than 1, divisible by 1 and themselves only
class MainTest(unittest.TestCase):
    def test_prime_num_generator(self):
       self.assertEqual(type(prime_num_generator(100)), list, msg="A list must be returned")
       self.assertTrue(isinstance(prime_num_generator(100)[-1], int), msg="Error: Integers must be written")
       self.assertTrue(prime_num_generator(100)[-2]>1, msg="A prime number cannot be less than 2")
       length = len(prime_num_generator(100))
       self.assertTrue(is_prime(random.choice(prime_num_generator(100))), msg="Number is not a prime number")


if __name__ == '__main__':
    unittest.main()