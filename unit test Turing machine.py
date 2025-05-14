import unittest
from Turing machine.py import accepts_0n1n0n1n  

class TestTuringMachinePattern(unittest.TestCase):

    def test_valid_inputs(self):
        self.assertTrue(accepts_0n1n0n1n("00110011"))  
        self.assertTrue(accepts_0n1n0n1n("0101"))      
        self.assertTrue(accepts_0n1n0n1n("000111000111")) 

    def test_invalid_inputs(self):
        self.assertFalse(accepts_0n1n0n1n("")) 
        self.assertFalse(accepts_0n1n0n1n("0001110011")) 
        self.assertFalse(accepts_0n1n0n1n("00110101"))    
        self.assertFalse(accepts_0n1n0n1n("0110"))        
        self.assertFalse(accepts_0n1n0n1n("001100"))      

if __name__ == "__main__":
    unittest.main()
