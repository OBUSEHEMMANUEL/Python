import unittest

from testing_testing.exception import MycustomException
from . import utils


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)  # add assertion here

    def test_add_fuc(self):
        x = utils.add(5, 7)
        self.assertEqual(12, x)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, 2)

    def test_that_add_throws_exception(self):
        with self.assertRaises(TypeError):
            utils.add(2, "hi")

        with self.assertRaises(MycustomException):
            utils.add(6, 2)


if __name__ == '__main__':
    unittest.main()
