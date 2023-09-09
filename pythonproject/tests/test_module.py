"""Import appropriate modules to select src filepath since it isnt in the test director"""
import unittest
import sys
import os


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)
"""Import files from src we want to test"""
from src import source_code
from src import lib
from src import desc_stat


class TestSourceCode(unittest.TestCase):
    """unit test class which will test source code"""

    def test_add(self):
        """Test the add function"""
        result = source_code.add(1, 1)
        expected_result = 2
        self.assertEqual(result, expected_result)

    def test_load_data_from_csv(self):
        """We will attempt to load some not very good csv files and some missing ones to ensure proper error handling"""
        result = lib.load_data_from_csv("notAfile.csv")
        expected_result = None
        self.assertEqual(result, expected_result)

        result = lib.load_data_from_csv("pythonproject\tests\testBreaker.md")
        expected_result = None
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
