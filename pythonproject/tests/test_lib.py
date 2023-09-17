"""Import appropriate modules to select src filepath since it isnt in the test director"""
import unittest
import sys
#import os
sys.path.append('pythonproject/src')
import lib


def load_frame():
    data = lib.load_data_from_csv("https://www.statlearning.com/s/Auto.csv")
    return data

class TestSourceCode(unittest.TestCase):
    """unit test class which will test source code"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = load_frame()

    def test_load_data_from_csv(self):
        """We will attempt to load some not very good csv files and some missing ones to ensure proper error handling"""
        result = lib.load_data_from_csv("notAfile.csv")
        expected_result = None
        self.assertEqual(result, expected_result)

        result = lib.load_data_from_csv("pythonproject\tests\testBreaker.md")
        expected_result = None
        self.assertEqual(result, expected_result)
    
    def test_min(self):
        result = lib.df_min(self.df,"weight")
        expected_result = 1613
        self.assertEqual(result,expected_result)

    def test_max(self):
        result = lib.df_max(self.df,"weight")
        expected_result = 5140
        self.assertEqual(result,expected_result)



if __name__ == "__main__":
    unittest.main()
