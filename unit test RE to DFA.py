import unittest
from automata.fa.dfa import DFA
from RE to DFA.py import regex_to_dfa  

class TestRegexToDFA(unittest.TestCase):

    def test_accept_valid_strings(self):
        dfa = regex_to_dfa("(a|b)*abb")
        self.assertTrue(dfa.accepts_input("abb"))
        self.assertTrue(dfa.accepts_input("aabb"))
        self.assertTrue(dfa.accepts_input("babb"))
        self.assertTrue(dfa.accepts_input("aaabb"))

    def test_reject_invalid_strings(self):
        dfa = regex_to_dfa("(a|b)*abb")
        self.assertFalse(dfa.accepts_input("ababa"))
        self.assertFalse(dfa.accepts_input("abab"))
        self.assertFalse(dfa.accepts_input("aab"))
        self.assertFalse(dfa.accepts_input("aabba"))

if __name__ == "__main__":
    unittest.main()
