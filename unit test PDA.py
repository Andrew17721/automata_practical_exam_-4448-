import unittest
from PDA.py import is_odd_palindrome  
class TestOddPalindrome(unittest.TestCase):

    def test_valid_odd_palindromes(self):
        self.assertTrue(is_odd_palindrome("aba"))
        self.assertTrue(is_odd_palindrome("abcba"))
        self.assertTrue(is_odd_palindrome("a"))
        self.assertTrue(is_odd_palindrome("madam"))
        self.assertTrue(is_odd_palindrome("racecar"))

    def test_invalid_or_even_length(self):
        self.assertFalse(is_odd_palindrome("abccba"))  
        self.assertFalse(is_odd_palindrome("abca"))     
        self.assertFalse(is_odd_palindrome("hello"))   
        self.assertFalse(is_odd_palindrome("aa"))      

if __name__ == "__main__":
    unittest.main()
