from sentence_transformers import SentenceTransformer
"""
To allow for offline use, the install script must trigger sentence_transformers 
to pull the model from the huggingface hub and cache it
"""
SentenceTransformer("all-MiniLM-L6-v2").encode("foo")