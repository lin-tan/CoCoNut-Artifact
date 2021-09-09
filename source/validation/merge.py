from source.validation.patch import Patch

from collections import defaultdict


def read_beam(beam_file, meta_data, model, context):
    lines = open(beam_file).read().split('\n')
    dataset = []

    for line in lines:
        if line.startswith('S'):  # start of new bug
            source = line.split('\t')[1]
            row_num = int(line.split('\t')[0].split('-')[1])
            defects4j_id = " ".join(meta_data[row_num])
            meta = "\t".join(meta_data[row_num])
        elif line.startswith('T'):
            target = line.split('\t')[1]
        elif line.startswith('H'):
            hypothesis = line.split('\t')[2]
            score = float(line.split('\t')[1])
            dataset.append(Patch(source, target, hypothesis, defects4j_id, row_num, score, meta, model, context))

    return dataset


def get_meta(meta):
    fin = open(meta, 'r')
    data = []
    for l in fin.readlines():
        data.append(l.split('\t'))
    return data


def merge():
    # open the 20 output.
    MAIN_DIR = "./intermediate_repo/python/results/"
    print(MAIN_DIR)
    meta_no_context_data = get_meta('./data/test/quixpy/nocontext/meta.txt')
    meta_context_data = get_meta('./data/test/quixpy/context/meta.txt')

    coconut1 = MAIN_DIR + 'quixpy_fconv_tuned_1/checkpoint_best.pt/output.tok.nbest.txt'
    coconut2 = MAIN_DIR + 'quixpy_fconv_tuned_2/checkpoint_best.pt/output.tok.nbest.txt'
    coconut3 = MAIN_DIR + 'quixpy_fconv_tuned_3/checkpoint_best.pt/output.tok.nbest.txt'
    coconut4 = MAIN_DIR + 'quixpy_fconv_tuned_4/checkpoint_best.pt/output.tok.nbest.txt'
    coconut5 = MAIN_DIR + 'quixpy_fconv_tuned_5/checkpoint_best.pt/output.tok.nbest.txt'
    coconut6 = MAIN_DIR + 'quixpy_fconv_tuned_6/checkpoint_best.pt/output.tok.nbest.txt'
    coconut7 = MAIN_DIR + 'quixpy_fconv_tuned_7/checkpoint_best.pt/output.tok.nbest.txt'
    coconut8 = MAIN_DIR + 'quixpy_fconv_tuned_8/checkpoint_best.pt/output.tok.nbest.txt'
    coconut9 = MAIN_DIR + 'quixpy_fconv_tuned_9/checkpoint_best.pt/output.tok.nbest.txt'
    coconut10 = MAIN_DIR + 'quixpy_fconv_tuned_10/checkpoint_best.pt/output.tok.nbest.txt'
    MAIN_DIR = "./intermediate_repo_good/python/results/"
    encore = [coconut1, coconut2, coconut3, coconut4, coconut5, coconut6, coconut7, coconut8, coconut9, coconut10]
    coconut1 = MAIN_DIR + 'quixpy_context_tuned_1/checkpoint_best.pt/output.tok.nbest.txt'
    coconut2 = MAIN_DIR + 'quixpy_context_tuned_2/checkpoint_best.pt/output.tok.nbest.txt'
    coconut3 = MAIN_DIR + 'quixpy_context_tuned_3/checkpoint_best.pt/output.tok.nbest.txt'
    coconut4 = MAIN_DIR + 'quixpy_context_tuned_4/checkpoint_best.pt/output.tok.nbest.txt'
    coconut5 = MAIN_DIR + 'quixpy_context_tuned_5/checkpoint_best.pt/output.tok.nbest.txt'
    coconut6 = MAIN_DIR + 'quixpy_context_tuned_6/checkpoint_best.pt/output.tok.nbest.txt'
    coconut7 = MAIN_DIR + 'quixpy_context_tuned_7/checkpoint_best.pt/output.tok.nbest.txt'
    coconut8 = MAIN_DIR + 'quixpy_context_tuned_8/checkpoint_best.pt/output.tok.nbest.txt'
    coconut9 = MAIN_DIR + 'quixpy_context_tuned_9/checkpoint_best.pt/output.tok.nbest.txt'
    coconut10 = MAIN_DIR + 'quixpy_context_tuned_10/checkpoint_best.pt/output.tok.nbest.txt'
    coconuts = [coconut1, coconut2, coconut3, coconut4, coconut5, coconut6, coconut7, coconut8, coconut9, coconut10]

    all_coconut = []
    for idx, enc_res in enumerate(encore):
        print(idx)
        all_coconut += read_beam(enc_res, meta_no_context_data, idx, "nocontext")
    for idx, coco_res in enumerate(coconuts):
        print(idx)
        all_coconut += read_beam(coco_res, meta_context_data, idx, "context")

    current_patch = ""

    for result in all_coconut:
        if current_patch != result.id:
            current_patch = result.id
            fout = open('/local1/mydir/all_results/quixpy/' +
                        current_patch.replace(" ", "").replace('\n', '').replace('/', '.') +
                        '_COCONUT_PERFECT_LOC.txt','w')
            count = 0
        if '$STRING$ $STRING$' not in result.patch and 'System . exit' not in result.patch:
            count += 1
            fout.write("START PATCH" + '\n')
            fout.write(current_patch)
            fout.write(str(result.patch) + '\n')
            fout.write(str(result.score) + '\n')
            fout.write(result.meta)
            fout.write(str(count) + '\n')

merge()