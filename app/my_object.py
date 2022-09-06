import os
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image
from typing import List
from PIL import Image


class CustomImageDataset(Dataset):
    def __init__(self, img_dir: List, transform=None):
        self.img_dir = img_dir
        self.transform = transform

    def __len__(self):
        return len(self.img_dir)

    def __getitem__(self, item):
        img = Image.open(self.img_dir[item])
        if self.transform:
            tensors = self.transform(img)
            return tensors
