import os
import random
import sys

import source.tokenization.tokenization as tokenization


def save_data(data, label, meta, path, name):
    print(path)
    foutd = open(path + name + "_remadd.txt", 'w', encoding='utf-8', errors='ignore')
    for i, d in enumerate(data):
        foutd.write(" ".join(d).replace('\n', '').replace('\t', '') +
                    '\t' + " ".join(label[i]).replace('\n', '').replace('\t', '') + '\n')
    foutm = open(path + name + "_meta.txt", 'w', encoding='utf-8', errors='ignore')
    for m in meta:
        foutm.write(m + '\n')


# https://stackoverflow.com/questions/23289547/shuffle-two-list-at-once-with-same-order
def unison_shuffled_copies(a, b, c):
    try:
        assert len(a) == len(b)
        assert len(a) == len(c)
        d = list(zip(a, b, c))
        random.shuffle(d)
        a, b, c = zip(*d)
        return a, b, c
    except:
        print("Error: Files with different length")
        print(len(a))
        print(len(b))
        print(len(c))
        sys.exit()


def get_training_testing(data, labels, meta_list, valid_size=20000, test_size=20000, shuffle=False):
    """
    Split the data between, training, valid and test set. Shuffled for training
    :param data:
    :param labels:
    :param meta_list:
    :param valid_size:
    :param test_size:
    :param shuffle:
    :return:
    """
    if shuffle:
        data, labels, meta_list = unison_shuffled_copies(data, labels, meta_list)
    train_data = data[:-(test_size + valid_size)]
    train_labels = labels[:-(test_size + valid_size)]
    train_meta = meta_list[:-(test_size + valid_size)]
    valid_data = data[-(test_size + valid_size):-test_size]
    valid_labels = labels[-(test_size + valid_size):-test_size]
    valid_meta = meta_list[-(test_size + valid_size):-test_size]
    test_data = data[-test_size:]
    test_labels = labels[-test_size:]
    test_meta = meta_list[-test_size:]
    return ([train_data, train_labels, train_meta],
            [valid_data, valid_labels, valid_meta],
            [test_data, test_labels, test_meta])


def main_nocontext(init_dir):
    """
    Parse and clean data without context.
    :param init_dir: dir with the original training data.
    :return:
    """
    saved_data_path = init_dir + "/../nocontext/train/"
    print("Save data in :", saved_data_path)

    # Check if path exist
    if not os.path.exists(saved_data_path):
        os.makedirs(saved_data_path)

    rem_path = os.path.join(init_dir, 'rem.txt')
    add_path = os.path.join(init_dir, 'add.txt')
    meta_path = os.path.join(init_dir, 'meta.txt')

    rem_lines = open(rem_path).read().split('\n')
    add_lines = open(add_path).read().split('\n')
    meta_lines = open(meta_path).read().split('\n')

    rem_toks = [tokenization.tokenize(line) for line in rem_lines]
    add_toks = [tokenization.tokenize(line) for line in add_lines]

    [train_data, train_labels, train_meta], \
    [valid_data, valid_labels, valid_meta], \
    [test_data, test_labels, test_meta] = get_training_testing(rem_toks, add_toks,
                                                               meta_lines,
                                                               shuffle=True)
    save_data(train_data, train_labels, train_meta, saved_data_path, '_train')
    save_data(valid_data, valid_labels, valid_meta, saved_data_path, '_valid')
    save_data(test_data, test_labels, test_meta, saved_data_path, '_test')


def main_context(init_dir):
    """
    Parse and clean data with context.
    :param init_dir:
    :return:
    """
    saved_data_path = init_dir + "/../context/train/"
    print("Save data in :", saved_data_path)
    # Check if path exist
    if not os.path.exists(saved_data_path):
        os.makedirs(saved_data_path)

    rem_path = os.path.join(init_dir, 'rem.txt')
    add_path = os.path.join(init_dir, 'add.txt')
    context_path = os.path.join(init_dir, 'context.txt')
    meta_path = os.path.join(init_dir, 'meta.txt')

    rem_lines = open(rem_path).read().split('\n')
    add_lines = open(add_path).read().split('\n')
    context_lines = open(context_path).read().split('\n')
    meta_lines = open(meta_path).read().split('\n')

    rem_toks = []
    rem_toks_init = [tokenization.tokenize(line) for line in rem_lines]
    add_toks = [tokenization.tokenize(line) for line in add_lines]
    context_toks = [tokenization.tokenize(line) for line in context_lines]
    print(rem_toks_init[0])
    print("CONTEXT")
    print(context_toks[0])
    for i in range(0, len(rem_toks_init)):
        try:

            if context_toks[i] and rem_toks_init[i]:
                rem_toks.append(rem_toks_init[i] + ['<CTX>'] + context_toks[i])
            elif rem_toks_init[i]:
                rem_toks.append(rem_toks_init[i])
            elif context_toks[i]:
                rem_toks.append(['<CTX>'] + context_toks[i])
            else:
                rem_toks.append([" "])
        except:
            continue

    [train_data, train_labels, train_meta], \
    [valid_data, valid_labels, valid_meta], \
    [test_data, test_labels, test_meta] = get_training_testing(rem_toks, add_toks,
                                                               meta_lines,
                                                               shuffle=True)
    save_data(train_data, train_labels, train_meta, saved_data_path, '_train')
    save_data(valid_data, valid_labels, valid_meta, saved_data_path, '_valid')
    save_data(test_data, test_labels, test_meta, saved_data_path, '_test')


def main(data_dir, context):
    print("Start tokenizing: ", context)
    if context == "context":
        main_context(data_dir)
    if context == "nocontext":
        print("Nocontext")
        main_nocontext(data_dir)


main(sys.argv[1], sys.argv[2])
