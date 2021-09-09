import source.testing.generate_split as generate_split
import sys


def defects4j_context(saved_data_path):
    """
    Prepare data for defects4j with context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/defects4j/origin/rem.txt'
    add_path = './data/test/defects4j/origin/add.txt'
    meta_path = './data/test/defects4j/origin/meta.txt'
    context_path = './data/test/defects4j/origin/context.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split_context(both_path, rem_path, add_path, meta_path, context_path, saved_data_path,
                                          valid_size, perfect_loc, only_test)


def defects4j_nocontext(saved_data_path):
    """
    Prepare data for defects4j without context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/defects4j/origin/rem.txt'
    add_path = './data/test/defects4j/origin/add.txt'
    meta_path = './data/test/defects4j/origin/meta.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split(both_path, rem_path, add_path, meta_path, saved_data_path, valid_size,
                                  perfect_loc, only_test)


def quixbug_nocontext(saved_data_path):
    """
    Test set for quixbug java without context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/quixjava/origin/rem.txt'
    add_path = './data/test/quixjava/origin/add.txt'
    meta_path = './data/test/quixjava/origin/meta.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split(both_path, rem_path, add_path, meta_path, saved_data_path, valid_size, perfect_loc, only_test)


def quixbug_context(saved_data_path):
    """
    Test set for quixbug java with context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/quixjava/origin/rem.txt'
    add_path = './data/test/quixjava/origin/add.txt'
    meta_path = './data/test/quixjava/origin/meta.txt'
    contex_path = './data/test/quixjava/origin/context.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split_context(both_path, rem_path, add_path, meta_path, contex_path, saved_data_path, valid_size, perfect_loc, only_test)


def bugaid_nocontext(saved_data_path):
    """
    BugAid test data no context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/bugaid/origin/rem.txt'
    add_path = './data/test/bugaid/origin/add.txt'
    meta_path = './data/test/bugaid/origin/meta.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split(both_path, rem_path, add_path, meta_path, saved_data_path, valid_size,
                                  perfect_loc, only_test)


def bugaid_context(saved_data_path):
    """
    BugAid test data context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/bugaid/origin/rem.txt'
    add_path = './data/test/bugaid/origin/add.txt'
    meta_path = './data/test/bugaid/origin/meta.txt'
    context_path = './data/test/bugaid/origin/context.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split_context(both_path, rem_path, add_path, meta_path, context_path, saved_data_path,
                                          valid_size, perfect_loc, only_test)


def quixpy_nocontext(saved_data_path):
    """
    Quixpy no context
    :param saved_data_path:
    :return:
    """
    both_path = './data/test/quixpy/origin/remadd.txt'
    meta_path = './data/test/quixpy/origin/meta.txt'
    rem_path = ''
    add_path = ''
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split(both_path, rem_path, add_path, meta_path, saved_data_path, valid_size,
                                  perfect_loc, only_test)


def quixpy_context(saved_data_path):
    """
    Quixpy data with context
    :param saved_data_path:
    :return:
    """
    both_path = './data/test/quixpy/origin/remadd.txt'
    rem_path = ''
    add_path = ''
    context_path = './data/test/quixpy/origin/context.txt'
    meta_path = './data/test/quixpy/origin/meta.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split_context(both_path, rem_path, add_path, meta_path, context_path,
                                          saved_data_path, valid_size, perfect_loc, only_test)


def manybugs_nocontext(saved_data_path):
    """
    Manybugs benchmark without context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/manybugs/origin/rem.txt'
    add_path = './data/test/manybugs/origin/add.txt'
    meta_path = './data/test/manybugs/origin/meta.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split(both_path, rem_path, add_path, meta_path, saved_data_path, valid_size,
                                  perfect_loc, only_test)


def manybugs_context(saved_data_path):
    """
    Manybugs benchmark with context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/manybugs/origin/rem.txt'
    add_path = './data/test/manybugs/origin/add.txt'
    meta_path = './data/test/manybugs/origin/meta.txt'
    context_path = './data/test/manybugs/origin/context.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split_context(both_path, rem_path, add_path, meta_path, context_path, saved_data_path,
                                          valid_size, perfect_loc, only_test)


def codeflaws_nocontext(saved_data_path):
    """
    CodeFlaws benchmark without context
    :param saved_data_path:
    :return:
    """
    both_path = ''
    rem_path = './data/test/codeflaws/origin/rem.txt'
    add_path = './data/test/codeflaws/origin/add.txt'
    meta_path = './data/test/codeflaws/origin/meta.txt'
    valid_size = 2000
    perfect_loc = True
    only_test = True
    generate_split.generate_split(both_path, rem_path, add_path, meta_path, saved_data_path,
                                  valid_size, perfect_loc, only_test)


def codrep4_nocontext(saved_data_path):
    both_path = ''
    rem_path = './data/test/codrep/origin/rem.txt'
    add_path = './data/test/codrep/origin/add.txt'
    meta_path = './data/test/codrep/origin/meta.txt'
    valid_size = 11000
    perfect_loc = True
    only_test = True
    generate_split.generate_split(both_path, rem_path, add_path, meta_path, saved_data_path, valid_size,
                                  perfect_loc, only_test)


def codrep4_context(saved_data_path):
    both_path = ''
    rem_path = './data/test/codrep/origin/rem.txt'
    add_path = './data/test/codrep/origin/add.txt'
    meta_path = './data/test/codrep/origin/meta.txt'
    context_path = './data/test/codrep/origin/context.txt'
    valid_size = 11000
    perfect_loc = True
    only_test = True
    generate_split.generate_split_context(both_path, rem_path, add_path, meta_path, context_path, saved_data_path,
                                          valid_size, perfect_loc, only_test)


if sys.argv[2] == 'defects4j':
    if sys.argv[3] == "nocontext":
        defects4j_nocontext(sys.argv[1])
    if sys.argv[3] == "context":
        defects4j_context(sys.argv[1])
if sys.argv[2] == 'quixbugs':
    if sys.argv[3] == "nocontext":
        quixbug_nocontext(sys.argv[1])
    if sys.argv[3] == "context":
        quixbug_context(sys.argv[1])
if sys.argv[2] == 'bugaid':
    if sys.argv[3] == "nocontext":
        bugaid_nocontext(sys.argv[1])
    if sys.argv[3] == "context":
        bugaid_context(sys.argv[1])
if sys.argv[2] == 'quixpy':
    if sys.argv[3] == "nocontext":
        quixpy_nocontext(sys.argv[1])
    if sys.argv[3] == "context":
        quixpy_context(sys.argv[1])
if sys.argv[2] == 'manybugs':
    if sys.argv[3] == "nocontext":
        manybugs_nocontext(sys.argv[1])
    if sys.argv[3] == "context":
        manybugs_context(sys.argv[1])
if sys.argv[2] == 'codeflaws':
    if sys.argv[3] == "nocontext":
        codeflaws_nocontext(sys.argv[1])
if sys.argv[2] == 'codrep':
    if sys.argv[3] == "nocontext":
        codrep4_nocontext(sys.argv[1])
    if sys.argv[3] == "context":
        codrep4_context(sys.argv[1])
