from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
from automata.regex.regex import Regex

def regex_to_dfa(regex: str) -> DFA:

    nfa: NFA = Regex(regex).to_epsilon_nfa()

    dfa: DFA = nfa.to_dfa()
    return dfa


dfa1 = regex_to_dfa("(a|b)*abb")
print(dfa1.accepts_input("aabb"))    
print(dfa1.accepts_input("ababa"))  
