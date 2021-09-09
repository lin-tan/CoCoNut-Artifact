import source.tokenization.tokenization as tokenization
import source.tokenization.generate_data as generate_data

import os


def save_data(data, label, meta, path, name):
    foutd = open(path + name + "_remadd.txt", 'w', encoding='utf-8', errors='ignore')
    for i, d in enumerate(data):
        foutd.write(" ".join(d).replace('\n', '').replace('\t', '') + '\t' + " ".join(label[i]).replace('\n', '').replace('\t', '') + '\n')
    foutm = open(path + name + "_meta.txt", 'w', encoding='utf-8', errors='ignore')
    for m in meta:
        foutm.write(m+'\n')


def get_training_testing(data, labels, meta_list, valid_size, test_size, shuffle=False):
    if shuffle:
        data, labels, meta_list = generate_data.unison_shuffled_copies(data, labels, meta_list)
        train_data = data[:-(test_size + valid_size)]
        train_labels = labels[:-(test_size + valid_size)]
        train_meta = meta_list[:-(test_size + valid_size)]
        valid_data = data[-(test_size + valid_size):-test_size]
        valid_labels = labels[-(test_size + valid_size):-test_size]
        valid_meta = meta_list[-(test_size + valid_size):-test_size]
        test_data = data[-test_size:]
        test_labels = labels[-test_size:]
        test_meta = meta_list[-test_size:]
    else:
        train_data = data[:-(test_size + valid_size)]
        train_labels = labels[:-(test_size + valid_size)]
        train_meta = meta_list[:-(test_size + valid_size)]
        valid_data = data[-(test_size + valid_size):-test_size]
        valid_labels = labels[-(test_size + valid_size):-test_size]
        valid_meta = meta_list[-(test_size + valid_size):-test_size]
        test_data = data[-test_size:]
        test_labels = labels[-test_size:]
        test_meta = meta_list[-test_size:]
    return([train_data, train_labels, train_meta],
           [valid_data, valid_labels, valid_meta],
           [test_data, test_labels, test_meta])


def generate_split_context(both_path, rem_path, add_path, meta_path, context_path, saved_data_path,
                                      valid_size, perfect_loc, only_test):
    rem_lines = []
    context_lines = []
    add_lines = []
    meta_lines = []

    if perfect_loc:
        if both_path != '':
            print(both_path)
            context_lines = open(context_path).read().split('\n')
            with open(both_path) as f:
                for line in f.read().split('\n'):
                    if line != '':
                        rem_line, add_line = line.split('\t')
                        rem_lines.append(rem_line)
                        add_lines.append(add_line)
        else:
            rem_lines = open(rem_path).read().split('\n')
            add_lines = open(add_path).read().split('\n')
            context_lines = open(context_path).read().split('\n')

        print(len(rem_lines))
        print(len(add_lines))
        print(len(context_lines))
        assert(len(rem_lines) == len(add_lines))

        if meta_path != '':
            meta_lines = open(meta_path).read().split('\n')
            print(len(meta_lines))
            assert(len(rem_lines) == len(meta_lines))
        else:
            meta_lines = ['']*len(rem_lines)

        init_rem_toks = [tokenization.tokenize(line) for line in rem_lines]
        add_toks = [tokenization.tokenize(line) for line in add_lines]
        context_toks = [tokenization.tokenize(line) for line in context_lines]
        rem_toks = []
        #print(context_toks[0])
        for i, line in enumerate(init_rem_toks):
            #print(context_toks[i])
            rem_toks.append(init_rem_toks[i] + ['<CTX>'] +  context_toks[i])

        #print(rem_toks[-1])
        if only_test:
            test_size = len(rem_toks)
            valid_size = 0
        [train_data, train_labels, train_meta], \
        [valid_data, valid_labels, valid_meta], \
        [test_data, test_labels, test_meta] = get_training_testing(rem_toks[:-1], add_toks[:-1],
                meta_lines[:-1],
                                                                                 valid_size=valid_size,
                                                                                 test_size=test_size,
                                                                                 shuffle=False)
        # dummy data to prevent errors in fairseq
        if only_test:
            train_data, train_labels, train_meta = test_data, test_labels, test_meta
            valid_data, valid_labels, valid_meta = test_data, test_labels, test_meta
            save_data(train_data, train_labels, train_meta, saved_data_path, '_train')
            save_data(valid_data, valid_labels, valid_meta, saved_data_path, '_valid')
            save_data(test_data, test_labels, test_meta, saved_data_path, '_test')

    else:
        for (dirpath, dirnames, filenames) in os.walk(both_path):
            for filename in filenames:
                fin = open(dirpath + '/' + filename)
                rem_lines = []
                add_lines = []
                meta_lines = []
                for line in fin.read().split('\n'):
                    if '$SUSPICION$' in line:
                        rem_line = line.split('$SUSPICION$')[0]
                        meta = line.split('$SUSPICION$')[1]
                        rem_lines.append(rem_line)
                        add_lines.append('')
                        meta_lines.append(meta)
                rem_toks = [tokenization.tokenize(line) for line in rem_lines]
                # add_toks incorrect. Only for consistency
                add_toks =  [tokenization.tokenize(line) for line in rem_lines]
                if only_test:
                    test_size = len(rem_toks)
                    valid_size = 0

                [train_data, train_labels, train_meta], \
                [valid_data, valid_labels, valid_meta], \
                [test_data, test_labels, test_meta] = get_training_testing(rem_toks, add_toks,
                                                                                     meta_lines,
                                                                                     valid_size=valid_size,
                                                                                     test_size=test_size,
                                                                                     shuffle=False)

                # dummy data to prevent errors in fairseq
                if only_test:
                    full_saved_data_path = saved_data_path + filename + 'dir/'

                    if not os.path.isdir(full_saved_data_path):
                        os.mkdir(full_saved_data_path)

                    train_data, train_labels, train_meta = test_data, test_labels, test_meta
                    valid_data, valid_labels, valid_meta = test_data, test_labels, test_meta
                    save_data(train_data, train_labels, train_meta, full_saved_data_path, '_train')
                    save_data(valid_data, valid_labels, valid_meta, full_saved_data_path, '_valid')
                    save_data(test_data, test_labels, test_meta, full_saved_data_path, '_test')




def generate_split(both_path, rem_path, add_path, meta_path, saved_data_path, valid_size, perfect_loc, only_test):
    rem_lines = []
    add_lines = []
    meta_lines = []

    if perfect_loc:
        print("perfect LOC")
        if both_path != '':
            print(both_path)
            with open(both_path) as f:
                for line in f.read().split('\n'):
                    if line != '':
                        rem_line, add_line = line.split('\t')
                        rem_lines.append(rem_line)
                        add_lines.append(add_line)
        else:
            rem_lines = open(rem_path).read().split('\n')
            add_lines = open(add_path).read().split('\n')

        print(len(rem_lines))
        print(len(add_lines))
        assert(len(rem_lines) == len(add_lines))

        if meta_path != '':
            meta_lines = open(meta_path).read().split('\n')
            print(len(meta_lines))
            assert(len(rem_lines) == len(meta_lines))
        else:
            meta_lines = ['']*len(rem_lines)

        rem_toks = [tokenization.tokenize(line) for line in rem_lines]
        add_toks = [tokenization.tokenize(line) for line in add_lines]
        if meta_path != "":
            assert(len(rem_toks) == len(meta_lines))
        if only_test:
            test_size = len(rem_toks)
            valid_size = 0

        [train_data, train_labels, train_meta], \
        [valid_data, valid_labels, valid_meta], \
        [test_data, test_labels, test_meta] = get_training_testing(rem_toks, add_toks,
                                                                                 meta_lines,
                                                                                 valid_size=valid_size,
                                                                                 test_size=test_size,
                                                                                 shuffle=False)

        
        # dummy data to prevent errors in fairseq
        if only_test:
            train_data, train_labels, train_meta = test_data, test_labels, test_meta
            valid_data, valid_labels, valid_meta = test_data, test_labels, test_meta
            save_data(train_data, train_labels, train_meta, saved_data_path, '_train')
            save_data(valid_data, valid_labels, valid_meta, saved_data_path, '_valid')
            save_data(test_data, test_labels, test_meta, saved_data_path, '_test')

    else:
        for (dirpath, dirnames, filenames) in os.walk(both_path):
            for filename in filenames:
                fin = open(dirpath + '/' + filename)
                rem_lines = []
                add_lines = []
                meta_lines = []
                for line in fin.read().split('\n'):
                    if '$SUSPICION$' in line:
                        rem_line = line.split('$SUSPICION$')[0]
                        meta = line.split('$SUSPICION$')[1]
                        rem_lines.append(rem_line)
                        add_lines.append('')
                        meta_lines.append(meta)
                rem_toks = [tokenization.tokenize(line) for line in rem_lines]
                # add_toks incorrect. Only for consistency
                add_toks =  [tokenization.tokenize(line) for line in rem_lines]
                if only_test:
                    test_size = len(rem_toks)
                    valid_size = 0

                [train_data, train_labels, train_meta], \
                [valid_data, valid_labels, valid_meta], \
                [test_data, test_labels, test_meta] = get_training_testing(rem_toks, add_toks,
                                                                                     meta_lines,
                                                                                     valid_size=valid_size,
                                                                                     test_size=test_size,
                                                                                     shuffle=False)

                # dummy data to prevent errors in fairseq
                if only_test:
                    full_saved_data_path = saved_data_path + filename + 'dir/'

                    if not os.path.isdir(full_saved_data_path):
                        os.mkdir(full_saved_data_path)

                    train_data, train_labels, train_meta = test_data, test_labels, test_meta
                    valid_data, valid_labels, valid_meta = test_data, test_labels, test_meta
                    save_data(train_data, train_labels, train_meta, full_saved_data_path, '_train')
                    save_data(valid_data, valid_labels, valid_meta, full_saved_data_path, '_valid')
                    save_data(test_data, test_labels, test_meta, full_saved_data_path, '_test')

