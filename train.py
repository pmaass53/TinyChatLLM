import os
import math
import time
import random

vocab = []
token_to_id = []
id_to_token = []
text = ""

# Load Tokens
with open("tokens.txt", "r", encoding="utf-8") as f:
    vocab = [t.strip() for t in f.readlines()]
    token_to_id = {t: i for i, t in enumerate(vocab)}
    id_to_token = {i: t for t, i in token_to_id.items()}

# Load Conversation
with open("tinychat.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Helper Functions
def tokenize(text):
    result = []
    for word in text.split():
        result.append(token_to_id.get(word, 0))
    return result

data = tokenize(text)
print(data)