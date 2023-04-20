#!/bin/sh

mkdir ./model_store ||
    torch-model-archiver \
        --model-name ROBERTA_QA \
        --version 1.0 \
        --serialized-file ./squad_model/pytorch_model.bin \
        --handler src/serve/transformer_handler_generalized \
        --extra-files "squad_model/config.json,./setup_config.json" \
        --export-path ./model_store \
        --force
