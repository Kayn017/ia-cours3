import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        self.assertEqual(False, False)


if __name__ == '__main__':
    unittest.main()
