import os
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image
from typing import List
from PIL import Image
import torchvision.transforms as T
import torch


class CustomImageDataset(Dataset):
    '''
    Специальный клас для датасета из картинок
    не оптимально сделана функция data, при больших объемах данных будет работать долго
    '''
    def __init__(self, img_dir: List, transform=None):
        self.img_dir = img_dir
        self.transform = transform

    def data(self):
        tensor_data = []
        for i in range(len(self.img_dir)):
            if i == 0:
                img = Image.open(self.img_dir[i])
                to_gray = T.functional.rgb_to_grayscale(img)
                to_resize = T.Resize(size=(5900, 8300))(to_gray)
                tensor0 = T.ToTensor()(to_resize)
            else:
                img = Image.open(self.img_dir[i])
                to_gray = T.functional.rgb_to_grayscale(img)
                to_resize = T.Resize(size=(5900, 8300))(to_gray)
                tensor1 = T.ToTensor()(to_resize)
                tensor0 = torch.cat((tensor0, tensor1))
        return tensor0

    def __len__(self):
        return len(self.img_dir)

    def __getitem__(self, item):
        img = Image.open(self.img_dir[item])
        if self.transform:
            tensors = self.transform(img)
            return tensors
