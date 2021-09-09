import multiprocessing as mp
import os
import subprocess
import sys
import threading
import time

from source.tokenization.tokenization import get_strings_numbers, token2statement
import shutil
import source.validation.quixbugs_test_suite as quixbugs_test_suite


class RunCmd(threading.Thread):
    # https://stackoverflow.com/questions/4158502/kill-or-terminate-subprocess-when-timeout?noredirect=1
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout
        self.out = b"TIMEOUT"
        self.err = b"TIMEOUT"

    def run(self):
        self.p = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        self.out, self.err = self.p.communicate()

    def Run(self):
        self.start()
        self.join(self.timeout)


        if self.is_alive():
            os.kill(self.p.pid, 0)
            self.p.kill()      #use self.p.kill() if process needs a kill -9
            self.join()
        return self.out, self.err


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


def clean_temp_folder(temp_dir):
    """
    :param temp_dir: temporary directory where the patch will be compiled
    :return: nothing
    """
    if os.path.isdir(temp_dir):
        for files in os.listdir(temp_dir):
            file_p = os.path.join(temp_dir, files)
            try:
                if os.path.isfile(file_p):
                    os.unlink(file_p)
                elif os.path.isdir(file_p):
                    shutil.rmtree(file_p)
            except Exception as e:
                print(e)
    else:
        os.makedirs(temp_dir)


def create_copy_quixbug(file_name, temp_dir, quixbug_dir):
    """
    Setup the copy of Quixbug for a specific bug
    :param file_name:
    :param temp_dir:
    :param quixbug_dir:
    :return:
    """
    shutil.copyfile(quixbug_dir + "Node.java", temp_dir + "Node.java")
    shutil.copyfile(quixbug_dir + "WeightedEdge.java", temp_dir + "WeightedEdge.java")
    shutil.copyfile(quixbug_dir + file_name, temp_dir + file_name)


def compile_fix(filename, temp_dir):
    # print(filename)

    p = subprocess.call(["javac",
                          temp_dir + "Node.java",
                          temp_dir + "WeightedEdge.java",
                          filename])
    #java_out1 = p.stdout.read()
    #print(java_out1)
    #p = subprocess.Popen(["javac",
    #                      temp_dir + "Node.java",
    #                      temp_dir + "WeightedEdge.java",
    #                      filename],
    #                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #p.wait()
    if p:
        return False
    else:
        return True


def insert_fix_quixbugs_several(file,  loc_start, loc_end, patch, temp_dir):
    temp_file = temp_dir + file
    patch_flag = False
    shutil.copyfile(temp_file, temp_file + '.bak')
    with open(temp_file, 'r') as file:
        try:
            data = file.readlines()
        except:
            data = ""
            return False
    count_tabs = 0
    final_patch = ""
    with open(temp_file, 'w') as file:
        for idx, line in enumerate(data):
            if idx >= loc_start -1 and idx <=  loc_end - 1 and patch_flag == False:
                file.write(patch)
                patch_flag = True
            elif idx >= loc_start -1 and idx <= loc_end -1 and patch_flag == True:
                continue
            else:
                file.write(line)
    return temp_file + '.bak'


def insert_fix_quixbugs(file, loc, patch, temp_dir):
    temp_file = temp_dir + file
    shutil.copyfile(temp_file, temp_file + '.bak')
    with open(temp_file, 'r') as file:
        try:
            data = file.readlines()
        except:
            data = ""
            return False
    count_tabs = 0
    final_patch = ""
    with open(temp_file, 'w') as file:
        for idx, line in enumerate(data):
            if idx == loc -1:

                for i, char in enumerate(data[idx]):
                    if char != ' ':
                        break
                    else:
                        count_tabs +=1
                for i in range(0, count_tabs):
                    final_patch += " "
                file.write(final_patch + patch)
            else:
                file.write(line)
    return temp_file + '.bak'


def read_result_file(inputs):
    print("start")
    start = time.time()
    result_file = inputs[0]
    init_temp_dir = inputs[1]
    quixbug_dir = '/local1/mydir/all_results/quixpy/QuixBugs/java_programs_bak/'
    shutil.copytree('/local1/mydir/all_results/quixpy/QuixBugs/', init_temp_dir)
    temp_folder = init_temp_dir + '/java_programs/'
    current_meta = ""
    with open(result_file, 'r') as fin:
        meta = ""
        lines = fin.read().split('\n')
    bug = result_file.split('/')[-1].rsplit('_',1)[0]
    print(bug)
    for i, line in enumerate(lines):
        if 'START PATCH' in line:
            source = lines[i+1]
            target = lines[i+2]
            tokenized_patch = lines[i + 3]
            #tokenized_patch = lines[i+3]
            id = lines[i+4]
            row_num = lines[i+5]
            score = lines[i+6]
            meta = lines[i+7]
            model = lines[i+8]
            context = lines[i+9]
            rank = lines[i+10]
            if tokenized_patch == source:
                continue
            else:
                if current_meta != meta:
                    current_meta = meta
                    print("Start working on new bug:")
                    print(meta)
                    if '-' not in meta.split('\t')[1].replace('\n', ''):
                        loc = int(meta.split('\t')[1].replace('\n', ''))
                    else:
                        loc = 0
                        start_loc, end_loc = meta.split('\t')[1].replace('\n', '').split('-')
                file = meta.split('\t')[0] + '.java'
                fout = open("quixjava_log_correct_context" + file + ".log", 'w')
                strings, numbers = get_meta_tokens(file, quixbug_dir)
                patches = token2statement(tokenized_patch.split(' '), numbers, strings)

                def test_patch(patches):
                    for patch in patches:
                        if "System.exit" in patch:
                            continue
                        print(patch)
                        clean_temp_folder(temp_folder)
                        create_copy_quixbug(file, temp_folder, quixbug_dir)
                        #exit()
                        if loc > 0:
                            original_file = insert_fix_quixbugs(file, loc, patch + '\n', temp_folder)
                        else:
                            original_file = insert_fix_quixbugs_several(file, int(start_loc), int(end_loc), patch + '\n',
                                                                        temp_folder)
                        res = compile_fix(temp_folder + file, temp_folder)
                        print(res)
                        if res:
                            print(patch)
                            pass_suite = quixbugs_test_suite.pass_test_suite(file.replace('.java', '').lower(),
                                                                             init_temp_dir)
                            print(pass_suite)
                            if pass_suite >= 0:
                                fout.write("Candidate patch: " + file.replace('.java', '') + "\n")
                                fout.write(patch + "\n")
                                fout.write("Target patch: " + "\n")
                                fout.write(target + "\n")
                                fout.write(str(rank) + "\n")
                                fout.write(str(score) + "\n")
                                fout.write(context + "\n")
                                fout.write(str(model) + "\n")
                                end = time.time()
                                fout.write("Time to validate:" + str(float(end) - float(start)) + " seconds" + "\n")
                                fout.flush()
                                return 0
                    return -1

                flag = test_patch(patches)
                if flag == 0:
                    break;


def main():
    all_args = []
    for (dirpath, dirnames, filenames) in os.walk('./intermediate_repo_good/java/2006/merged_quixjava/'):
        for filename in filenames:
            if any(x in filename for x in ["TOPOLOGICAL_ORDERING"]):
                all_args.append([dirpath + filename, '/local1/mydir/temp_QUIXBUG/' + filename + '/quixbugs/'])
    print("command")
    pool = mp.Pool(10)
    result = pool.map(read_result_file, all_args)

main()
