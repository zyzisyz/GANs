#!/usr/bin/env python
# coding=utf-8

import os
from torchvision.datasets import MNIST
from pytorch_lightning.core import LightningModule, LightningDataModule
import torchvision.transforms as transforms
from torch.utils.data import DataLoader


class MNISTDataModule(LightningDataModule):
    def __init__(self, batch_size: int = 64, data_path: str = os.getcwd(), num_workers: int = 4):
        super().__init__()
        self.batch_size = batch_size
        self.data_path = data_path
        self.num_workers = num_workers

        self.transform = transforms.Compose([transforms.ToTensor(),
                                             transforms.Normalize([0.5], [0.5])])
        self.dims = (1, 28, 28)

    def prepare_data(self, stage=None):
        # Use this method to do things that might write to disk or that need to be done only from a single GPU
        # in distributed settings. Like downloading the dataset for the first time.
        MNIST(self.data_path, train=True, download=True, transform=transforms.ToTensor())

    def setup(self, stage=None):
        # There are also data operations you might want to perform on every GPU, such as applying transforms
        # defined explicitly in your datamodule or assigned in init.
        self.mnist_train = MNIST(self.data_path, train=True, transform=self.transform)

    def train_dataloader(self):
        return DataLoader(self.mnist_train, batch_size=self.batch_size, num_workers=self.num_workers)

