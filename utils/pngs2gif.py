#!/usr/bin/env python

import os

import imageio
from argparse import ArgumentParser


def png2gif(source, gifname, time):
    print("png2gif: from {} to {}...".format(source, gifname))
    file_list = os.listdir(source)
    file_list.sort()
    file_list = [os.path.join(source, png) for png in file_list]

    frames = []
    for png in file_list:
        print(png)
        frames.append(imageio.imread(png))
    imageio.mimsave(gifname, frames, 'GIF', duration=time)


if __name__ == "__main__":
    argparser = ArgumentParser()

    argparser.add_argument("--figs_dir", default="figs", type=str)
    argparser.add_argument("--gif_path", default="result.gif", type=str)
    argparser.add_argument("--time", default=0.3, type=float)
    args = argparser.parse_args()

    png2gif(args.figs_dir, args.gif_path, args.time)


