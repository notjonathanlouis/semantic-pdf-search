import torch
import torch.nn as nn
from transformers import BertConfig, BertModel


class MiniBertEncoder(nn.Module):
    """
    Wrapper that mimics SentenceTransformer's `modules[0]` layout:
        self.auto_model -> BertModel
    """
    def __init__(self):
        super().__init__()

        cfg = BertConfig(
            vocab_size=30522,
            hidden_size=384,
            num_hidden_layers=6,
            num_attention_heads=12,
            intermediate_size=1536,
            max_position_embeddings=512,
            type_vocab_size=2,
            hidden_act="gelu",
            initializer_range=0.02
        )
        self.auto_model = BertModel(cfg)

    def forward(self, input_ids, attention_mask=None, token_type_ids=None):
        """
        Returns the pooled CLS embedding (same tensor that ST would feed into its pooling head,
        if one were present).
        """
        out = self.auto_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
            token_type_ids=token_type_ids,
        )
        return out.pooler_output  # shape: (batch, 384)


def load_checkpoint(path: str) -> MiniBertEncoder:
    """
    Instantiate the module, strip the `0.auto_model.` prefix from keys, and load weights.
    """
    # 1. Build the naked model
    model = MiniBertEncoder()

    # 2. Convert key names so they match the sub-module hierarchy we just defined
    raw_state = torch.load(path, map_location="cpu")
    cleaned_state = {
        k.replace("0.auto_model.", "auto_model."): v
        for k, v in raw_state.items()
    }

    # 3. Load (will raise if anything is missing or unexpected)
    model.load_state_dict(cleaned_state, strict=True)

    return model
