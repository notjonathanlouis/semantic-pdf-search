from main import Searcher, SentenceEncoder, SentenceTransformer
import torch
search = Searcher.forPDF(
    SentenceEncoder(SentenceEncoder.MODEL1), 
    "pdfs/signals.pdf")

model = SentenceTransformer("all-MiniLM-L6-v2")


torch.save(model.state_dict(), "model.pth")