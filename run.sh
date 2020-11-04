#!/bin/bash

rm -rf figs
mkdir figs

python main.py \
	--num_workers 32 \
	--log_every_n_steps 1 \
	--gpus 1 \
	--figs figs

