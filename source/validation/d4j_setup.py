import subprocess
import os
import shutil

def clean_temp_folder(temp_dir):
    """
    :param temp_dir: temporary directory where the patch will be compiled
    :return: nothing
    """
    print(temp_dir)
    if os.path.isdir(temp_dir):
        os.system('rm -fr "%s"' % temp_dir)
    os.makedirs(temp_dir)



def clean_temp_folder_bak(temp_dir):
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


def load_defects4j_project(project, bug_id, temp_dir):
    FNULL = open(os.devnull, 'w')
    command = "/local/mydir/defects4j/framework/bin/defects4j " + " checkout " + " -p " + project + " -v " + bug_id + " -w " + temp_dir
    print(command)
    p = subprocess.Popen([command], shell=True, stdout=FNULL, stderr=FNULL)
    p.wait()
    return True