import codecs
import os
import subprocess
import sys
import time

from source.tokenization.tokenization import get_strings_numbers, token2statement
import shutil
import source.validation.d4j_setup as d4j_setup


def command(cmd, timeout=250):
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    t_beginning = time.time()
    while True:
        if p.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            p.terminate()
            return 'TIMEOUT', 'TIMEOUT'
        time.sleep(1)
    out, err = p.communicate()
    return out, err


def compile_fix(temp_folder):
    os.chdir(temp_folder)
    p = subprocess.Popen(["/local/tlutelli/defects4j/framework/bin/defects4j", "compile"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if "FAIL" in str(err) or "FAIL" in str(out):
        res = False
    else:
        res = True
    return res


def defects4j_test_suite(temp_folder, timeout=250):
    os.chdir(temp_folder)
    out, err = command(["/local/tlutelli/defects4j/framework/bin/defects4j", "test", "-r"],
                       timeout)
    return out, err


def defects4j_trigger(temp_folder, timeout=250):
    os.chdir(temp_folder)
    out, err = command(["/local/tlutelli/defects4j/framework/bin/defects4j", "export", "-p", "tests.trigger"],
                       timeout)
    return out, err


def defects4j_test_one(temp_folder, test_case, timeout=250):
    os.chdir(temp_folder)
    out, err = command(["/local/tlutelli//defects4j/framework/bin/defects4j", "test", "-t", test_case],
                       timeout)
    return out, err


def get_meta_tokens(file, temp_dir, loc_start, loc_end):
    temp_file = temp_dir + file
    numbers_set = {}
    strings_set = {}
    with open(temp_file, 'r') as file:
        data = file.readlines()
        for idx, line in enumerate(data):
            if not (loc_start <= idx + 1 <= loc_end):
                continue
            dist = max(abs(loc_start - idx - 1), abs(loc_end - idx - 1))
            strings, numbers = get_strings_numbers(line)
            for num in numbers:
                if num != '0' and num != '1':
                    if num in numbers_set:
                        numbers_set[num] = min(dist, numbers_set[num])
                    else:
                        numbers_set[num] = dist
            for str in strings:
                if str in strings_set:
                    strings_set[str] = min(dist, strings_set[str])
                else:
                    strings_set[str] = dist
    final_strings = []
    final_numbers = []
    for k, v in numbers_set.items():
        final_numbers.append([k, v])
    for k, v in strings_set.items():
        final_strings.append([k, v])
    final_numbers.sort(key=lambda x: x[1])
    final_strings.sort(key=lambda x: x[1])
    return final_strings, final_numbers


def insert_fix_defects4j(file, loc_start, loc_end, patch, temp_dir):
    temp_file = temp_dir + file
    shutil.copyfile(temp_file, temp_file + '.bak')
    with open(temp_file, 'r') as file:
        data = file.readlines()
    patch_flag = False
    with open(temp_file, 'w') as file:
        for idx, line in enumerate(data):
            if loc_start - 1 <= idx <= loc_end - 1 and patch_flag is False:
                file.write(patch)
                patch_flag = True
            elif loc_start - 1 <= idx <= loc_end - 1 and patch_flag is True:
                continue
            else:
                file.write(line)
    return temp_file + '.bak'


def read_result_file(result_file, temp_dir):

    print("start")
    result_file_name = result_file.split('/')[-1]
    project = result_file_name.split('.TAB.')[0]
    bug_id = result_file_name.split('.TAB.')[1]
    file_name = result_file_name.split('.TAB.')[2].replace('.SEP.', '/')
    if len(result_file_name.split('.TAB.')) == 4:
        start_line = int(result_file_name.split('.TAB.')[3].split('_')[0])
        end_line = start_line
    elif len(result_file_name.split('.TAB.')) == 5:
        start_line = int(result_file_name.split('.TAB.')[3].split('_')[0])
        end_line = int(result_file_name.split('.TAB.')[4].split('_')[0])
    else:
        return
    # Check if output logs already exist:
    if os.path.exists("d4jlogs/" + result_file_name + ".log"):
        fin = open("d4jlogs/" + result_file_name + ".log", 'r')
        lines = fin.readlines()
        if len(lines) > 0 and "DONE" in lines[-1]:
            return
    fout = open("d4jlogs/" + result_file_name + ".log", 'w')


    fp = codecs.open(result_file, 'r', 'utf-8')
    lines = fp.readlines()
    fp.close()

    d4j_setup.clean_temp_folder(temp_dir)
    d4j_setup.load_defects4j_project(project, bug_id + 'b', temp_dir)
    if project == "Mockito":
        print("Mockito needs separate compilation")
        test = compile_fix(temp_dir)

    start_time = time.time()
    out_init, err_init = defects4j_test_suite(temp_dir)
    standard_time = int(time.time() - start_time)

    failed_test_cases = str(out_init).split(' - ')[1:]
    for i, failed_test_case in enumerate(failed_test_cases):
        failed_test_cases[i] = failed_test_case.strip()
    out_length = len(failed_test_cases)
    print(out_length, str(standard_time) + 's')

    validated_patch = set()
    tokenized_patch_num = 0
    real_rank = 0
    start_time = time.time()
    for i, line in enumerate(lines):
        if 'START PATCH' in line:
            real_rank += 1
            source = lines[i+1]
            target = lines[i+2]
            #tokenized_patch = lines[i + 2]
            tokenized_patch = lines[i+3]
            id = lines[i+4]
            row_num = lines[i+5]
            score = lines[i+6]
            meta = lines[i+7]
            model = lines[i+8]
            context = lines[i+9]
            rank = lines[i+10]
            file = file_name
            if int(real_rank) % 10 == 0:
                print(project + " " + str(bug_id) + ": " + str(real_rank) + '\n')

            strings, numbers = get_meta_tokens(file, temp_dir, start_line, end_line)
            strings = [item[0] for item in strings][:5]
            numbers = [item[0] for item in numbers][:5]
            patches = token2statement(tokenized_patch.split(' '), numbers, strings)
            tokenized_patch_num += 1
            for patch in patches[:5]:
                if len(validated_patch) > 20000:
                    return
                patch = patch.strip()
                if patch in validated_patch:
                    continue
                validated_patch.add(patch)

                original_file = insert_fix_defects4j(file, start_line, end_line, patch + '\n', temp_dir)
                if project == 'Mockito':
                    compile_fix(temp_dir)

                out, err = defects4j_test_suite(temp_dir, timeout=min(300, standard_time*3))
                #print(out)
                #print(err)
                if "Failing tests: 0" in str(out):
                    fout.write("Candidate patch: " + project + " " + bug_id + "\n")
                    fout.write(patch + "\n")
                    fout.write("Target patch: " + "\n")
                    fout.write(target + "\n")
                    fout.write(str(real_rank) + "\n")
                    fout.write(str(score) + "\n")
                    fout.write(context + "\n")
                    fout.write(str(model) + "\n")
                    end = time.time()
                    fout.write("Time to validate:" + str(float(end) - float(start_time)) + " seconds" + "\n")
                    fout.write("DONE")
                    fout.flush()
                    return
                elif len(str(out).split(' - ')[1:]) < out_length and "BUILD FAILED" not in str(err):
                    failed_test_for_patches = str(out).split(' - ')[1:]
                    print(failed_test_for_patches)
                    test = True
                    for failed_test_for_patch in failed_test_for_patches:
                        failed_test_for_patch = failed_test_for_patch.strip()
                        if failed_test_for_patch not in failed_test_cases:
                            test = False
                            break
                    if test:
                        out_length = len(failed_test_for_patches)
                        fout.write("Partial Candidate patch: " + project + " " + bug_id + "\n")
                        fout.write(patch + "\n")
                        fout.write("Target patch: " + "\n")
                        fout.write(target + "\n")
                        fout.write(str(real_rank) + "\n")
                        fout.write(str(score) + "\n")
                        fout.write(context + "\n")
                        fout.write(str(model) + "\n")
                        end = time.time()
                        fout.write("Number of failed test cases: " + str(out_length))
                        fout.write("Failled Test Cases:")
                        fout.write("; ".join(failed_test_for_patches) + "\n")
                        fout.write("Time to validate:" + str(float(end) - float(start_time)) + " seconds" + "\n")
                        fout.flush()
                shutil.copyfile(original_file, original_file.replace('.bak', ''))
    fout.write("DONE")
    return


read_result_file(sys.argv[1], sys.argv[2])
