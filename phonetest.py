import unittest
from numbers import sentence_maker

# i can have this return all letter combos, all letter combos containing real words, or just the words contained in the combos

class PhoneTestCase(unittest.TestCase):

    def test_phone_number(self):
        expectedResult = set(['nip', 'oh', 'sac', 'is', 'mi', 'pa', 'grab', 'sa'])
        self.assertEqual(sentence_maker(6104701212), expectedResult)

    # def test_num_of_possibilities(self):
    #     self.assertEqual(len(sentence_maker(6104701212)), 324)

    def test_small_num(self):
        self.assertEqual(sentence_maker(24), set(['ah']))

if __name__ == '__main__':
    unittest.main()