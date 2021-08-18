# for utilities function

import torch

def prepare_input(self, word):
    alphabets = 'abcdefghijklmnopqrstvuwxyz'
    vector = [0 for x in range(26)]
    for c in word:
        vector[alphabets.index(c)] = 1
    return torch.tensor(vector)