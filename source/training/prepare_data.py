import os
import subprocess
import sys

from source.training.split_remadd import split_exclude


def main(language, train_dir, fairseq_dir):
    fairseq = os.environ['FAIRSEQPY']
    print("Pre-processing data for :", language)
    if not os.path.exists(fairseq_dir):
        os.makedirs(fairseq_dir)
    split_exclude(train_dir + 'exclude.txt', train_dir + '_train_remadd.txt', train_dir + '_train_meta.txt',
                  fairseq_dir + 'train.src', fairseq_dir + 'train.trg', fairseq_dir + 'train.meta')
    split_exclude(train_dir + 'exclude.txt', train_dir + '_valid_remadd.txt', train_dir + '_valid_meta.txt',
                  fairseq_dir + 'valid.src', fairseq_dir + 'valid.trg', fairseq_dir + 'valid.meta')
    cmd = 'python ' + fairseq + 'preprocess.py ' + '--source-lang src --target-lang trg --workers 40 ' + \
          '--trainpref ' + fairseq_dir + 'train ' + \
          '--validpref ' + fairseq_dir + 'valid ' + \
          '--testpref ' + fairseq_dir + 'valid ' + \
          '--destdir ' + fairseq_dir + 'bin'
    subprocess.call(cmd, shell=True)


def main_context(language, train_dir, fairseq_dir):
    fairseq = os.environ['FAIRSEQPY']
    print("Pre-processing data for :", language)
    if not os.path.exists(fairseq_dir):
        os.makedirs(fairseq_dir)
    split_exclude(train_dir + 'exclude.txt', train_dir + '_train_remadd.txt', train_dir + '_train_meta.txt',
                  fairseq_dir + 'train.src', fairseq_dir + 'train.trg', fairseq_dir + 'train.meta')
    split_exclude(train_dir + 'exclude.txt', train_dir + '_valid_remadd.txt', train_dir + '_valid_meta.txt',
                  fairseq_dir + 'valid.src', fairseq_dir + 'valid.trg', fairseq_dir + 'valid.meta')
    cmd = 'python ' + fairseq + 'preprocess.py ' + '--source-lang src --target-lang trg --workers 40 ' + \
          '--trainpref ' + fairseq_dir + 'train ' + \
          '--validpref ' + fairseq_dir + 'valid ' + \
          '--testpref ' + fairseq_dir + 'valid ' + \
          '--destdir ' + fairseq_dir + 'bin'
    subprocess.call(cmd, shell=True)


if sys.argv[4] == 'nocontext':
    train_dir = sys.argv[2] + "/../nocontext/train/"
    fairseq_dir = sys.argv[3] + "/nocontext/train/"
    main(sys.argv[1], train_dir, fairseq_dir)
if sys.argv[4] == 'context':
    train_dir = sys.argv[2] + "/../context/train/"
    fairseq_dir = sys.argv[3] + "/context/train/"
    main_context(sys.argv[1], train_dir, fairseq_dir)
