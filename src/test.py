import unittest
from main import *
import re

class TestNewModel(unittest.TestCase):

    def test_basic(self):
        model = SentenceEncoder(SentenceEncoder.MODEL1)
        corpus = Corpus(["Andrew Jackson", "variability","speedy","rainfall", "Hegel", "Moon landing", "the capital of mexico", "obama", "mourning for a bygone era", "maroon"])
        search = Searcher(model, corpus) 
        self.assertEqual(search("red"), [len(corpus.texts) - 1])

    def test_pdf(self):
        model = SentenceEncoder(SentenceEncoder.MODEL1)
        search = Searcher.forPDF(model, "pdfs/compilers.pdf")
        self.assertEqual(search("lex with regex"), [41])

    def test_rerank_pdf(self):
        model = RerankingEncoder(SentenceEncoder.MODEL1, RerankingEncoder.MODEL1)
        search = Searcher.forPDF(model, "pdfs/compilers.pdf")
        print(search("lex with regex"))
        #self.assertEqual(search("lex with regex"), [41])

if __name__ == "__main__":
    unittest.main()