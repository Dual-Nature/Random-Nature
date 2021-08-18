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



from mpl_toolkits import mplot3d
import csv
import numpy as np
import matplotlib.pyplot as plt

with open('./word_list.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row).split(','))

fig = plt.figure()
ax = plt.axes(projection='3d')