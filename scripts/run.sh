#!/bin/bash

rm -rf figs
rm -rf ckpt
mkdir figs
mkdir ckpt

python main.py \
    --dataset mnist \
    --niter 10 \
    --dataroot ./ \
    --workers 8 \
    --batchSize 32 \
    --images figs \
    --ckpt ckpt \
    --cuda
