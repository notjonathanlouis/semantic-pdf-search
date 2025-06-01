import random
from math import *
from torch import Tensor
import torch
from sentence_transformers import SentenceTransformer
from abc import ABC
import pypdf
from typing import Optional


MODEL1 = "all-MiniLM-L6-v2"
MODEL2 = "all-mpnet-base-v2"


class AbstractTextEncoder(ABC):

    def __call__(self, text : str) -> Tensor:
        ...

    def search(self,query : str, database : list[str], top_k : Optional[int] = 1) -> list[int]:
        """
        Search for a query in a database of strings, returns the index of the highest ranking string in the database
        """
        query_enc = self(query)
        db_enc = [self(item) for item in database]
        # we can do this better
        similarities  = torch.Tensor([cosine_sim(query_enc, v) for v in db_enc])
        return torch.sort(similarities, descending=True)[1].tolist()[:top_k]
    
    def search_for_page(self, query : str, path : str, top_k : Optional[int] = 1) -> list[int]:
        texts = pdf_to_texts(path)
        return self.search(query, texts, top_k)

class RandomTextEncoder(AbstractTextEncoder):


    def __str__(self) -> str:
        return "Random Encoder"

    def __call_(self, text : str) -> Tensor:
        return torch.rand((1000,))
    

class SentenceTransformerTextEncoder(AbstractTextEncoder):

    def __init__(self, model_name : str) -> None:
        self.name = model_name
        self.model = SentenceTransformer(model_name)
        
    def __str__(self) -> str:
        return self.name

    def __call__(self, text : str) -> Tensor:
        return self.model.encode(text, convert_to_tensor=True)





def pdf_to_texts(path : str) -> list[str]:
    """
    Transforms a PDF into a list of strings, where each string is a page from the pdf
    """
    reader = pypdf.PdfReader(path)
    return [page.extract_text() for page in reader.pages]


def magnitude(v : Tensor) -> Tensor:
    return torch.linalg.norm(v)

def cosine_sim(rhs : Tensor, lhs : Tensor) -> Tensor: 
    return torch.dot(rhs, lhs)/(magnitude(rhs) * magnitude(lhs))

if __name__ == "__main__":
    enc = RandomTextEncoder()
    print(enc("foo"))

