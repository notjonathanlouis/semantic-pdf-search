import unittest
from main import *
from typing import Any

tests = 0
class TestAll(unittest.TestCase):

    def assertHasPage(self, enc : AbstractTextEncoder, query : str, path : str, expected_page : int, top_k : int = 5):
        real_pages = enc.search_for_page("what pins are SWD debugging on", path, top_k)
        self.assertIn(expected_page, real_pages)
        print(f"Passed, query: {query} got {real_pages}, expected {expected_page}")
    

    def test_basic(self):
        words = ["london", "paris", "washington dc", "apple"]
        search = "uk"
        enc = SentenceTransformerTextEncoder(MODEL1)
        self.assertEqual(enc.search(search, words), [0])
        words = ["""Functional programs express loops and other control flow by function calls.
                  Where Program 15.7b has a while loop, Program 15.12 has a function call to doListX""",
                  """For the best performance and stability across typical operating temperature ranges, use the Abracon ABM8-272-T3. 
                  You can source the ABM8-272-T3 directly from Abracon or from an authorised reseller""" 
                  """Kranz et al. [1986] performed escape analysis to determine which closures can be 
                  stack-allocated because they do not outlive their creating function and also 
                  integrated closure analysis with register allocation to make a high-performance optimizing compiler. """, 
                  """As we need only 3.3V for this design, we need to lower the
                  incoming 5V USB supply, in this case, using a second, external LDO voltage regulator. The NCP1117 (U1) chosen here
                  has a fixed output of 3.3V, is widely available, and can provide up to 1A of current, which will be plenty for most designs."""]
        search = "what oscillator to use in high temperature applications"
        self.assertEqual(enc.search(search, words), [1])


    def test_search_for_page(self):
        enc = SentenceTransformerTextEncoder(MODEL1)
        self.assertHasPage(enc, "what pins are SWD debugging on", "pdfs/rp2040.pdf", 23, top_k = 1) 
        self.assertHasPage(enc, "why does the rp2040 not have flash memory on chip", "pdfs/rp2040.pdf", 9, top_k=40)    

if __name__ == "__main__":
    unittest.main()
    