# SNNA reffered as Simple Neural Network Analyser
# import torch
import torch.nn as nn
import torch.nn.functional as F

class model(nn.Module):
    def __init__(self) -> None:
        super(model, self).__init__()
        self.sl1 = nn.Linear(26,12)
        self.sl2 = nn.Linear(12,9)

    def forward(self, x):
        x = F.relu(self.sl1(x))
        return F.relu(self.sl2(x))

