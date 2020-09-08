import unittest

from main import calcular

class Test(unittest.TestCase):

    def test_calcular(self):
        self.assertEqual(True, calcular(6, True))


if __name__ == '__main__':
    unittest.main()