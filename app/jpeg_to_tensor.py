import warnings
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as T
from IPython.display import clear_output
from PIL import Image
from matplotlib import cm
from time import perf_counter
from torch.utils.data import DataLoader
from tqdm import tqdm
from pathlib import Path
import glob
from my_object import CustomImageDataset


Image.MAX_IMAGE_PIXELS = None
warnings.filterwarnings('ignore')

plt.rc('font', size=30)

output_dir = Path(__file__).parent.parent / 'output'
file_list = glob.glob(f'{str(output_dir)}\\*.jpg')

data = CustomImageDataset(img_dir=file_list)

transform = T.Compose(
    [
        T.ToTensor()
    ]
)
data1 = CustomImageDataset(img_dir=file_list, transform=transform)

print(data1)
