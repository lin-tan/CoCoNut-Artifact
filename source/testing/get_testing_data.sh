#!/usr/bin/env bash
opts=$1
src_dict=$2
trg_dict=$3
src_dir=$4
trg_dir=$5

if [[ $opts == "process"  ]]; then
    fairseq_dir=./fairseq-context_good
    echo "preprocessing data"
    python source/testing/split_remadd.py $src_dir/_train_remadd.txt $trg_dir/train.src  $trg_dir/train.trg $src_dir/_train_meta.txt   $trg_dir/meta.txt
    python source/testing/split_remadd.py $src_dir/_valid_remadd.txt $trg_dir/valid.src $trg_dir/valid.trg $src_dir/_valid_meta.txt  $trg_dir/meta.txt
    python source/testing/split_remadd.py $src_dir/_test_remadd.txt $trg_dir/test.src $trg_dir/test.trg $src_dir/_test_meta.txt  $trg_dir/meta.txt

    python $fairseq_dir/preprocess.py --source-lang src --target-lang trg  --testpref $trg_dir/test --destdir $trg_dir/bin --tgtdict $trg_dict --srcdict $src_dict
fi