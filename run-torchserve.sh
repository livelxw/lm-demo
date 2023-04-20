#!/bin/sh

torchserve --start --model-store model_store --models my_tc=ROBERTA_QA.mar --ncs
