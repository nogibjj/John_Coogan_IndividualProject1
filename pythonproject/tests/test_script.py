"""Import appropriate modules to select src filepath since it isnt in the test director"""
import unittest
import sys
import os
sys.path.append('pythonproject/src')
import desc_stat
import lib

def load_frame():
    data = lib.load_data_from_csv("https://www.statlearning.com/s/Auto.csv")
    return data

class TestSourceCode(unittest.TestCase):
    """unit test class which will test source code"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.df = load_frame()
    
    def test_plot_save(self):
        file_to_check = 'scatter_plot_Weight vs MPG.png'
        self.assertTrue(os.path.exists("pythonproject/figures/scatter_plot_Weight vs MPG.png"),f"The file '{file_to_check}' did not get created.")


if __name__ == "__main__":
    unittest.main()
