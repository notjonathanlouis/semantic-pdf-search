from main import *
from time import time
from dataclasses import dataclass
from tqdm import tqdm

@dataclass
class BenchmarkResult:
    score : float
    runtime : float



class Benchmarker:

    def __init__(self, encoders : list[AbstractModel], suite : dict[str, dict[str, int]]):
        self.encoders = encoders      
        self.suite = suite

    def run_for(self, enc : AbstractModel) -> BenchmarkResult:
        times = []
        scores = []
        for pdf in tqdm(self.suite, desc = "PDFS", position=1):
            for query in tqdm(self.suite[pdf], desc = "Query", position=2):
                searcher = Searcher.forPDF(enc, f"pdfs/{pdf}")
                expected_page = self.suite[pdf][query]
                start_time = time()
                ranked_pages = searcher(query, None)
                times.append(time() - start_time)
                scores.append(1 - (ranked_pages.index(expected_page)/len(ranked_pages)))
        return BenchmarkResult(sum(scores)/len(scores), sum(times)/len(times))

    def run_all(self) -> dict[str, BenchmarkResult]:
        out = {}
        for encoder in tqdm(self.encoders, desc = "Models", position=0):
            out[str(encoder)] = self.run_for(encoder)
        return out
        
BENCHMARK = {
    "n32.pdf":{
        "what is the maximum system clock speed" : 74,
        "what is the default system clock speed" : 78,
        "how to change the default system clock speed" :78, 
        "what pins are SPI1 on": 116,
        "steps to configure PLL sysclk": 76,
    },
    "st77.pdf":{
       "rgb ordering command" : 142,
       "change vertical scrolling area": 137,
       "change the RGB format of the image": 150,
       "row address order": 142,
    },
    "rp2040.pdf" : {
        "what pins are SWD debugging on" : 23,
        "why does the rp2040 need a separate flash memory chip" : 9,
    },
    "k&r.pdf": {
        "What function gets a line from a file": 146,
        "Built in sort function" : 231,
        "## concat tokens" : 209
    },
    "compilers.pdf" : {
        "lex with regex": 41
    }
}


if __name__ == "__main__":
    benchmarker = Benchmarker([RerankingEncoder(SentenceEncoder.MODEL1, RerankingEncoder.MODEL1), SentenceEncoder(SentenceEncoder.MODEL1)], BENCHMARK)
    print(benchmarker.run_all())
