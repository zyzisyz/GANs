"""
To run this template just do:
python generative_adversarial_net.py

After a few epochs, launch TensorBoard to see the images being generated at every batch:

tensorboard --logdir default
"""
import os
from argparse import ArgumentParser, Namespace

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F  # noqa
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
import torchvision.utils as vutils

from pytorch_lightning.core import LightningModule, LightningDataModule
from pytorch_lightning.trainer import Trainer

from models import MNISTDataModule, GAN


def main(args: Namespace) -> None:
    # ------------------------
    # 1 INIT LIGHTNING MODEL
    # ------------------------
    model = GAN(args)

    # ------------------------
    # 2 INIT TRAINER
    # ------------------------
    # If use distubuted training  PyTorch recommends to use DistributedDataParallel.
    # See: https://pytorch.org/docs/stable/nn.html#torch.nn.DataParallel
    dm = MNISTDataModule.from_argparse_args(args)

    trainer = Trainer.from_argparse_args(args)

    # ------------------------
    # 3 START TRAINING
    # ------------------------
    trainer.fit(model, dm)


if __name__ == '__main__':
    parser = ArgumentParser()

    # Add program level args, if any.
    # ------------------------
    # Add LightningDataLoader args
    parser = MNISTDataModule.add_argparse_args(parser)
    # Add model specific args
    parser = GAN.add_argparse_args(parser)
    # Add trainer args
    parser = Trainer.add_argparse_args(parser)
    # Parse all arguments
    args = parser.parse_args()

    main(args)
