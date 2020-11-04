#!/bin/bash

python -u utils/pngs2gif.py \
	--figs_dir figs \
	--gif_path result.gif \
	--time 0.1

python -m http.server 
