import unittest
import stats as Stats
import random

class StatsTest(unittest.TestCase):

    s = Stats()
    lyst = []

    def test_0_median(self, lyst):
        print("Start medium test: ")
        for i in range(1, 10):
            lyst = random.sample(range(i), 10)
            self.assertEqual(lyst)

if __name__ == '__main__':
    unittest.main()