#!/bin/sh

python src/train_qa.py \
    --model_name_or_path ./model \
    --dataset_name squad \
    --max_train_samples 1000 \
    --do_train \
    --do_eval \
    --per_device_train_batch_size 12 \
    --learning_rate 3e-5 \
    --num_train_epochs 2 \
    --max_seq_length 384 \
    --doc_stride 128 \
    --output_dir ./squad_model/ \
    --overwrite_output_dir
