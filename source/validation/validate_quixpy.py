import os
import shutil
import sys
import time

from source.tokenization.tokenization import get_strings_numbers, token2statement
from source.validation.patch import Patch
from source.validation.run_cmd import RunCmd


def read_beam(beam_file, meta_data, model, context):
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

    return all_coconut


graph_based = ["breadth_first_search",
               "depth_first_search",
               "detect_cycle",
               "minimum_spanning_tree",
               "reverse_linked_list",
               "shortest_path_length",
               "shortest_path_lengths",
               "shortest_paths",
               "topological_ordering"
               ]


def get_meta_tokens(file, temp_dir):
    temp_file = temp_dir + file
    final_strings = []
    final_numbers = []
    with open(temp_file, 'r') as file:
        try:
            data = file.readlines()
        except:
            data = ""
            return False
        for idx, line in enumerate(data):
            strings, numbers = get_strings_numbers(line)
            for num in numbers:
                if num != '0' and num != '1':
                    final_numbers.append(num)
            final_strings += strings
    final_numbers = list(set(final_numbers))
    final_strings = list(set(final_strings))
    return final_strings, final_numbers


def setup_quixbugs(temp_dir, quixbug_main):
    quixbug_dir = quixbug_main + 'python_programs/'
    temp_file_dir = temp_dir + '/python_programs/'
    shutil.copytree(quixbug_main, temp_dir)
    return quixbug_dir, temp_file_dir


def insert_fix_quixbugs(file, loc, patch, temp_dir):
    temp_file = temp_dir + file
    shutil.copyfile(temp_file, temp_file + '.bak')
    with open(temp_file, 'r') as file:
        try:
            data = file.readlines()
        except Exception as e:
            print(e)
            data = ""
            return False
    count_tabs = 0
    final_patch = ""
    with open(temp_file, 'w') as file:
        for idx, line in enumerate(data):
            if idx == loc - 1:

                for i, char in enumerate(data[idx]):
                    if char != ' ':
                        break
                    else:
                        count_tabs += 1
                for i in range(0, count_tabs):
                    final_patch += " "
                file.write(final_patch + patch)
            else:
                file.write(line)
    return temp_file + '.bak'

fout = open("quixpy_log_correct_context.log", 'w')
temp_dir = "/local/mydir/all_results/quixpy/temp/"
quixdir = "/local/mydir/all_results/quixpy/QuixBugs/"
all_data = merge()
all_data.sort(key=lambda x: (x.id, x.rank, -x.score))
current_meta = ""
quixbug_dir, temp_file_dir = setup_quixbugs(temp_dir, quixdir)
all_patches = []
for p in all_data:
    tokenized_patch = p.patch
    target = p.target
    if tokenized_patch not in all_patches:
        all_patches.append(tokenized_patch)
        #print(p.meta)
        meta = p.meta
        if current_meta != meta:
            start = time.time()
            current_meta = meta
            fout.write("Start working on new bug: ")
            fout.write(meta)
            fout.flush()
            rank = 0
            found = 0
        if found == 0:
            buggy_file = meta.lower().split('\t')[0] + '.py'
            loc = int(meta.split("\t")[-1].replace("\n", ""))
            rank += 1
            strings, numbers = get_meta_tokens(buggy_file, temp_file_dir)
            patches = token2statement(tokenized_patch.split(' '), numbers, strings)
            print(rank, file=sys.stderr)
            #print(p.score, file=sys.stderr)

            def test_patch(patches):
                for patch in patches:
                    #print(patch, file=sys.stderr)
                    original_file = insert_fix_quixbugs(buggy_file, loc, patch + '\n', temp_file_dir)
                    os.chdir(temp_dir)
                    out, err = RunCmd(["python", "python_tester.py", buggy_file.replace('.py', '')], 30).Run()
                    #print(out.decode(), file=sys.stderr)
                    #print(err.decode(), file=sys.stderr)
                    good_python = []
                    bad_python = []
                    if meta.lower().split()[0] in graph_based:
                        allres = out.decode().split('CUT\n')
                        if len(allres) > 1: # double check that there is an output
                            clean = allres[0]
                            buggy = allres[1]
                            print(clean)
                            print(buggy)
                            if clean == buggy:
                                fout.write("Candidate patch: " + buggy_file.replace('.py', '') + "\n")
                                fout.write(patch + "\n")
                                fout.write("Target patch: " + "\n")
                                fout.write(target + "\n")
                                fout.write(str(rank) + "\n")
                                fout.write(str(p.score) + "\n")
                                fout.write(p.context + "\n")
                                fout.write(str(p.model) + "\n")
                                end = time.time()
                                fout.write("Time to validate:" + str(float(end) - float(start)) + " seconds" + "\n")
                                fout.flush()
                                return 1
                    elif "Correct Patch" in out.decode() and "Bad Patch" not in out.decode():
                        fout.write("Candidate patch: " + buggy_file.replace('.py', '') + "\n")
                        fout.write(patch + "\n")
                        fout.write("Target patch: " + "\n")
                        fout.write(target + "\n")
                        fout.write(str(rank) + "\n")
                        fout.write(str(p.score) + "\n")
                        fout.write(p.context + "\n")
                        fout.write(str(p.model) + "\n")
                        end = time.time()
                        fout.write("Time to validate:" + str(float(end) - float(start)) + " seconds" + "\n")
                        fout.flush()
                        return 1

                return 0

            found = test_patch(patches)

