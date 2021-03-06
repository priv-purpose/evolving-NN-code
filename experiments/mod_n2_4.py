from __future__ import print_function
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.autograd import Variable
import torchvision.datasets as dset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torchvision.models as models
import sys
import math
import argparse
from torchvision import datasets, transforms
import torchvision
import torchvision.transforms as transforms
from basic_blocks import *

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.layer1_0_0 = VGGBlock(3, 64, 2)
        self.layer3_1_1 = VGGBlock(64, 256, 4)
#forward
        self.avgpool_end = nn.AvgPool2d(8, stride=1)
        self.linear_end = nn.Linear(256,10)
    def forward(self, x):
        out = self.layer1_0_0(x)
        out = self.layer3_1_1(out)
#return
        out = self.avgpool_end(out)
        out = out.view(out.size(0), -1)
        out = self.linear_end(out)
        return out
