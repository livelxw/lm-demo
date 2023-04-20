#!/bin/sh

python ./src/model_mlm.py \
    --dataset_name wikitext \
    --dataset_config_name wikitext-2-raw-v1 \
    --max_train_samples 1000 \
    --output_dir model \
    --config_name roberta-base \
    --tokenizer_name roberta-base \
    --do_train \
    --do_eval \
    --overwrite_output_dir
