from torch.utils.data import Dataset
from typing import List
from PIL import Image
import torchvision.transforms as T
import torch


class CustomImageDataset(Dataset):
    """
    Специальный клас для датасета из картинок большого формата
    не оптимально сделана функция data, при больших объемах данных будет работать долго
    """

    def __init__(self, img_dir: List, transform: object = None, train: bool = False):
        super().__init__()
        self.img_dir = img_dir
        self.transform = transform
        self.train = train

    def data(self):
        pass

    def __len__(self):
        return len(self.img_dir)

    # noinspection PyUnusedLocal
    def __getitem__(self, item):
        self.img = Image.open(self.img_dir[item])
        if self.transform:
            self.img = self.transform(Image.open(self.img_dir[item]))
        return self.img
