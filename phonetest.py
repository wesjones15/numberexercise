import unittest
from numbers import sentence_maker

class PhoneTestCase(unittest.TestCase):

    def test_phone_number(self):
        self.assertEqual(sentence_maker(6104701212), [["m", "n", "o"],["g", "h", "i"],["p", "q", "r", "s"],["a", "b", "c"],["a", "b", "c"]])

    def test_num_of_possibilities(self):
        possibilities = 1
        for i in range(len(sentence_maker(6104701212))):
            possibilities *= len(sentence_maker(6104701212)[i])
        self.assertEqual(possibilities, 324)

    def test_small_num(self):
        self.assertEqual(sentence_maker(24), [["a","b","c"],["g","h","i"]])

if __name__ == '__main__':
    unittest.main()