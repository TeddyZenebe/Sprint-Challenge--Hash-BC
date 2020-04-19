import unittest

from ex1 import get_indices_of_item_weights


class TestEx1(unittest.TestCase):

    def test_ex1_1(self):
        weights_1 = [9]
        answer_1 = get_indices_of_item_weights(weights_1, 1, 9)
        self.assertTrue(answer_1 is None)

    def test_ex1_2(self):
        weights_2 = [4, 4]
        answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
        self.assertTrue(answer_2[0] == 1)
        self.assertTrue(answer_2[1] == 0)

    def test_ex1_3(self):
        weights_3 = [4, 6, 10, 15, 16]
        answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
        self.assertTrue(answer_3[0] == 3)
        self.assertTrue(answer_3[1] == 1)

    


if __name__ == '__main__':
    unittest.main()
