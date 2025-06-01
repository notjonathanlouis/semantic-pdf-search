import random
from math import *
from torch import Tensor
import torch
from sentence_transformers import SentenceTransformer
from abc import ABC
import pypdf
from typing import Optional
import os
import pickle

class AbstractEncoder(ABC):

    def __call__(self, text : str) -> Tensor: ...


class SentenceEncoder(AbstractEncoder):

    MODEL1 = "all-MiniLM-L6-v2"
    MODEL2 = "all-mpnet-base-v2"

    def __init__(self, model_name : str) -> None:
        self.name = model_name
        self.model = SentenceTransformer(model_name)
        
    def __str__(self) -> str:
        return self.name

    def __call__(self, text : str) -> Tensor:
        return self.model.encode(text, convert_to_tensor=True)





def hash_str(text : str):
    h = 5381
    r = 0xFFFFFFFFFFFFFFFF
    for c in text:
        h = ((h << 5) + h + ord(c)) & r
    return h

class Corpus:

    def __init__(self, texts : list[str]):
        self.texts = texts

    def __hash__(self) -> int:
        out = 1594430266020640378
        for text in self.texts:
            out ^= hash_str(text)
        return out
    

class Searcher:

    def __init__(self, 
                 model : AbstractEncoder,
                 corpus : Corpus,
                 path : str = "embeddings"):
        
        self.model = model
        self.corpus = corpus
        self.encodings = self.__load_embeddings(path)

    def __load_embeddings(self,path : str) -> Tensor:
        OPEN = True
        if path not in os.listdir("."):
            os.mkdir(f"./{path}")
        corpus_hash = hash(self.corpus)
        file_path = f"./{path}/{corpus_hash}"
        if OPEN and f"{corpus_hash}" in os.listdir(f"./{path}"):
            with open(file_path, "rb") as f:
                return pickle.load(f)
        else:
            enc = torch.stack([self.model(text) for text in self.corpus.texts], dim = 1)
            with open(file_path, "wb") as f:
                pickle.dump(enc, f)
            return enc

    @staticmethod
    def forPDF(model : AbstractEncoder, path : str) -> "Searcher":
        reader = pypdf.PdfReader(path)
        corpus = Corpus([page.extract_text() for page in reader.pages])
        return Searcher(model, corpus)

    def __call__(self, query : str, top_k : Optional[int] = 1) -> list[int]:
        """
        Searches for ``query`` in the corpus, returns the results index
        """

        query_enc = torch.stack([self.model(query)] * self.encodings.shape[1], dim = 1)
        similarities = torch.cosine_similarity(query_enc, self.encodings, dim = 0)
        print(torch.sort(similarities, descending=True)[1])
        return torch.sort(similarities, descending=True)[1][:top_k].tolist()
    

