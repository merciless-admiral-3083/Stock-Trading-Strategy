import unittest
import pandas as pd

class TestDataValidation(unittest.TestCase):

    def setUp(self):
        # Load the data
        file_path = '../data/HINDALCO_1D.xlsx'
        self.df = pd.read_excel(file_path)
    
    def test_data_types(self):
        # Test if 'open', 'high', 'low', 'close' are floats
        self.assertTrue(pd.api.types.is_float_dtype(self.df['open']), "Open should be a decimal.")
        self.assertTrue(pd.api.types.is_float_dtype(self.df['high']), "High should be a decimal.")
        self.assertTrue(pd.api.types.is_float_dtype(self.df['low']), "Low should be a decimal.")
        self.assertTrue(pd.api.types.is_float_dtype(self.df['close']), "Close should be a decimal.")
        
        # Test if 'volume' is an integer
        self.assertTrue(pd.api.types.is_integer_dtype(self.df['volume']), "Volume should be an integer.")
        
        # Test if 'instrument' is a string
        self.assertTrue(pd.api.types.is_string_dtype(self.df['instrument']), "Instrument should be a string.")
        
        # Test if 'datetime' is a datetime object
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.df['datetime']), "Datetime should be of datetime type.")

if __name__ == '__main__':
    unittest.main()
