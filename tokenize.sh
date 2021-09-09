#!/bin/bash
lang=$1
data_repo=$2
context=$3
fairseq_repo=$4
start=$5


# Tokenize
if [ "${start}" -lt 1 ]; then
    echo "Start tokenization"
    python -m source.tokenization.generate_data "${data_repo}" "${context}"
    echo "End tokenization"
fi

export FAIRSEQPY=./fairseq-context_good/

# Prepare data
if [ "${start}" -lt 2 ]; then
    echo "${context}"
    source activate pytorch
    python -m source.training.prepare_data "${lang}" "${data_repo}" "${fairseq_repo}" "${context}"
    source deactivate

fi



