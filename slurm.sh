#!/usr/bin/env sh
mkdir -p log
now=$(date +"%Y%m%d_%H%M%S")
srun --partition=Data --gres=gpu:4 --ntasks-per-node=1  --job-name=maskdetect python train.py --data data/mask.data --cfg cfg/yolov3-tiny-mask.cfg --epochs 100 2>&1|tee log/train-$now.log
