import time

from source.validation.patch import Patch
import os
from collections import defaultdict


def read_beam(beam_file, meta_data, model, context):
    """
    Read beam only for Quixjava meta
    :param beam_file:
    :param meta_data:
    :param model:
    :param context:
    :return:
    """
    lines = open(beam_file).read().split('\n')
    dataset = []

    for line in lines:
        if line.startswith('S'):  # start of new bug
            rank = 1
            source = line.split('\t')[1]
            row_num = int(line.split('\t')[0].split('-')[1])
            id = " ".join(meta_data[row_num])
            meta = "\t".join(meta_data[row_num])
        elif line.startswith('T'):
            target = line.split('\t')[1]
        elif line.startswith('H'):
            hypothesis = line.split('\t')[2]
            score = float(line.split('\t')[1])
            dataset.append(Patch(source, target, hypothesis, id, row_num, score, meta, model, context, rank))
            rank += 1
    return dataset


def get_meta(meta):
    fin = open(meta, 'r')
    data = []
    for l in fin.readlines():
        data.append(l.split('\t'))
    return data


def merge():
    # open the 20 output.
    MAIN_DIR = "./intermediate_repo/java/2006/results/"
    print(MAIN_DIR)
    meta_no_context_data = get_meta('./data/test/defects4j/nocontext/meta.txt')
    meta_context_data = get_meta('./data/test/defects4j/context/meta.txt')

    coconut1 = MAIN_DIR + 'd4j_fconv_tuned_1/checkpoint_best.pt/output.tok.nbest.txt'
    coconut2 = MAIN_DIR + 'd4j_fconv_tuned_2/checkpoint_best.pt/output.tok.nbest.txt'
    coconut3 = MAIN_DIR + 'd4j_fconv_tuned_3/checkpoint_best.pt/output.tok.nbest.txt'
    coconut4 = MAIN_DIR + 'd4j_fconv_tuned_4/checkpoint_best.pt/output.tok.nbest.txt'
    coconut5 = MAIN_DIR + 'd4j_fconv_tuned_5/checkpoint_best.pt/output.tok.nbest.txt'
    coconut6 = MAIN_DIR + 'd4j_fconv_tuned_6/checkpoint_best.pt/output.tok.nbest.txt'
    coconut7 = MAIN_DIR + 'd4j_fconv_tuned_7/checkpoint_best.pt/output.tok.nbest.txt'
    coconut8 = MAIN_DIR + 'd4j_fconv_tuned_8/checkpoint_best.pt/output.tok.nbest.txt'
    coconut9 = MAIN_DIR + 'd4j_fconv_tuned_9/checkpoint_best.pt/output.tok.nbest.txt'
    coconut10 = MAIN_DIR + 'd4j_fconv_tuned_10/checkpoint_best.pt/output.tok.nbest.txt'

    MAIN_DIR = "./intermediate_repo_good/java/2006/results/"

    encore = [coconut1, coconut2, coconut3, coconut4, coconut5, coconut6, coconut7, coconut8, coconut9, coconut10]
    coconut1 = MAIN_DIR + 'd4j_context_tuned_1/checkpoint_best.pt/output.tok.nbest.txt'
    coconut2 = MAIN_DIR + 'd4j_context_tuned_2/checkpoint_best.pt/output.tok.nbest.txt'
    coconut3 = MAIN_DIR + 'd4j_context_tuned_3/checkpoint_best.pt/output.tok.nbest.txt'
    coconut4 = MAIN_DIR + 'd4j_context_tuned_4/checkpoint_best.pt/output.tok.nbest.txt'
    coconut5 = MAIN_DIR + 'd4j_context_tuned_5/checkpoint_best.pt/output.tok.nbest.txt'
    coconut6 = MAIN_DIR + 'd4j_context_tuned_6/checkpoint_best.pt/output.tok.nbest.txt'
    coconut7 = MAIN_DIR + 'd4j_context_tuned_7/checkpoint_best.pt/output.tok.nbest.txt'
    coconut8 = MAIN_DIR + 'd4j_context_tuned_8/checkpoint_best.pt/output.tok.nbest.txt'
    coconut9 = MAIN_DIR + 'd4j_context_tuned_9/checkpoint_best.pt/output.tok.nbest.txt'
    coconut10 = MAIN_DIR + 'd4j_context_tuned_10/checkpoint_best.pt/output.tok.nbest.txt'
    coconuts = [coconut1, coconut2, coconut3, coconut4, coconut5, coconut6, coconut7, coconut8, coconut9, coconut10]

    all_coconut = []
    for idx, enc_res in enumerate(encore):
        print(idx)
        all_coconut += read_beam(enc_res, meta_no_context_data, idx, "nocontext")
    for idx, coco_res in enumerate(coconuts):
        print(idx)
        all_coconut += read_beam(coco_res, meta_context_data, idx, "context")

    return all_coconut

def main():
    all_patches = merge()
    all_patches.sort(key=lambda x: (x.id, x.rank, -x.score))
    current_meta = ""
    foutlog = open("d4j_log_correct_context.log", 'w')

    for patch in all_patches:
        meta = patch.meta
        if current_meta != meta:
            unique_patches = []
            current_meta = meta
            foutlog.write("Start working on new bug: ")
            foutlog.write(meta)
            foutlog.flush()
            file_name_no_java = ".TAB.".join(meta.split('\t')).replace("\n",'').replace('/','.SEP.')
            fout = open('./intermediate_repo_good/java/2006/merged_d4j/' +
                        file_name_no_java + "_results.txt", 'w')
        if patch.patch not in unique_patches:
            unique_patches.append(patch.patch)
            fout.write("START PATCH\n")

            fout.write(patch.source + "\n")
            fout.write(patch.target + "\n")
            fout.write(patch.patch + "\n")
            fout.write(patch.id)
            fout.write(str(patch.row_num) + "\n")
            fout.write(str(patch.score) + "\n")
            fout.write(patch.meta)
            fout.write(str(patch.model) + "\n")
            fout.write(patch.context + "\n")
            fout.write(str(patch.rank) + "\n")


main()
