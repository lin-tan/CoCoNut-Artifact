# make classes for extra classes and then just parse them in
# make version for proper programs

import subprocess
import types
import os

INIT_DIR = "/home/mydir/workspace/coconut/"


def prettyprint(o):
    if isinstance(o, types.GeneratorType):
        return("(generator) " + str(list(o)))
    else:
        return(str(o))


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


def pass_test_suite(algo, QUIXBUG_MAIN_DIR):
        FNULL = open(os.devnull, 'w')
        #try:
        os.chdir(QUIXBUG_MAIN_DIR)
        if algo == "reverse_linked_list":
            p1 = subprocess.Popen(["/usr/bin/javac", "-cp", ".:java_programs:junit.jar:hamcrest-all-1.3.jar",
                                   "java_testcases/" + algo.upper() + "_TEST.java"],
                                  stdout=subprocess.PIPE, stderr=FNULL, universal_newlines=True)
            java_out1 = p1.stdout.read()
            print(java_out1)
            p2 = subprocess.Popen(
                ["/usr/bin/java", "-cp", ".:java_programs:junit.jar:hamcrest-all-1.3.jar", "org.junit.runner.JUnitCore",
                 "java_testcases." + algo.upper() + "_TEST"],
                stdout=subprocess.PIPE, stderr=FNULL, universal_newlines=True)

            p1 = subprocess.Popen(["/usr/bin/javac", "-cp", ".:java_programs:junit.jar:hamcrest-all-1.3.jar",
                                   "java_testcases/" + algo.upper() + "_TEST.java"],
                                  stdout=subprocess.PIPE, stderr=FNULL, universal_newlines=True)
            java_out1 = p1.stdout.read()
            print(java_out1)
            p2 = subprocess.Popen(
                ["/usr/bin/java", "-cp", ".:java_programs:junit.jar:hamcrest-all-1.3.jar", "org.junit.runner.JUnitCore",
                 "java_testcases." + algo.upper() + "_TEST"],
                stdout=subprocess.PIPE, stderr=FNULL, universal_newlines=True)
        else:
            p1 = subprocess.Popen(["/usr/bin/javac", "-cp", ".:java_programs:junit.jar:hamcrest-all-1.3.jar", "java_testcases/junit/" + algo.upper() + "_TEST.java"],
                                  stdout=subprocess.PIPE, stderr=FNULL, universal_newlines=True)
            java_out1 = p1.stdout.read()
            print(java_out1)
            p2 = subprocess.Popen(["/usr/bin/java", "-cp", ".:java_programs:junit.jar:hamcrest-all-1.3.jar", "org.junit.runner.JUnitCore", "java_testcases.junit." + algo.upper() + "_TEST"],
                                  stdout=subprocess.PIPE, stderr=FNULL, universal_newlines=True)
            java_out = p2.stdout.read()
            print(java_out)
        if "FAILURES" in java_out:
            os.chdir(INIT_DIR)
            return -1
        else:
            return 1

        #except Exception as e:
        #    print(e)
        #    return -1
        #finally:
        os.chdir(INIT_DIR)
