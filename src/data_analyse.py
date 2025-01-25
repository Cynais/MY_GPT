
from pathlib import Path
import torch

script_dir = Path(__file__).resolve().parent

project_dir = script_dir.parent

data_file = project_dir / "data" / "raw" / "input.txt"

with data_file.open( 'r', encoding='utf-8') as f:
    text = f.read()
    
print("La longeur du dataset en character est de: ", len(text))

chars = sorted(list(set(text)))
vocab_size = len(chars)
print(''.join(chars))
print(chars)
print(vocab_size)

char2idx = {u:i for i, u in enumerate(chars)}
idx2char = {i:u for i, u in enumerate(chars)}

text_as_int = lambda text: [char2idx[c] for c in text]
int_as_text = lambda int: "".join([idx2char[c] for c in int])

print(text_as_int("Bonjour je test ma fonction d'encodage"))
print(int_as_text(text_as_int("Bonjour je test ma fonction d'encodage et decodage")))






