import unittest
from new import *

class TestNewModel(unittest.TestCase):

    def test_basic(self):
        model = SentenceEncoder(SentenceEncoder.MODEL1)
        corpus = Corpus(["Andrew Jackson", "variability","speedy","rainfall", "Hegel", "Moon landing", "the capital of mexico", "obama", "mourning for a bygone era", "maroon"])
        search = Searcher(model, corpus) 
        self.assertEqual(search("red"), [len(corpus.texts) - 1])

if __name__ == "__main__":
    unittest.main()