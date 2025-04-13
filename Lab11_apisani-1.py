# Lab11_apisani-1.py
# Alex Pisani
# Aug 5 2024
# takes a numeric degree value and normalizes it if more than a full rotation is entered

import unittest

def normalize_rotation(degrees):
    return degrees % 360 

class TestNormalizeRotation(unittest.TestCase):
    
    def test_normalize_rotation_100(self): # 100 stays 100 after normalization
        self.assertEqual(normalize_rotation(100), 100)
    
    def test_normalize_rotation_460(self): # -360 degrees normalizes to 100
        self.assertEqual(normalize_rotation(460), 100)

if __name__ == '__main__':
    unittest.main()