import unittest
import lecture_4p3

class TestStdDevOfLengths(unittest.TestCase):
    def test_case_1(self):
        L = ['a', 'z', 'p']
        self.assertEqual(lecture_4p3.stdDevOfLengths(L), 0)
        
    def test_case_2(self):
        L = ['apples', 'oranges', 'kiwis', 'pineapples']
        self.assertAlmostEqual(lecture_4p3.stdDevOfLengths(L), 1.8708, places=4)
        
    def test_case_3(self):
        L = ['eejsh', '', 'nujwwingbvfix', 'u', 'cbqool', 'hl', 'ksxwncnmr', 'nkqzqoxyxm']
        self.assertAlmostEqual(lecture_4p3.stdDevOfLengths(L), 4.3517, places=4)
        
    def test_case_4(self):
        L = ['rpabv']
        self.assertEqual(lecture_4p3.stdDevOfLengths(L), 0)
        
    def test_case_5(self):
        L = ['alebvbfcew', '']
        self.assertEqual(lecture_4p3.stdDevOfLengths(L), 5.0)
        
if __name__ == '__main__':
    unittest.main()