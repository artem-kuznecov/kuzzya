import unittest
from Builder import *

class TestBuilder(unittest.TestCase):
    def Test_builder(self):
        builder = ()
        self.assertEqual(builder.create(), None)

    def test_wheels(self):
        builder = CarBuilder()
        self.assertEqual(builder.wheels(), None)
        

if __name__ == "__main__":
    unittest.main()        

    