import os.path


def split_exclude(exclude_path, src_f_path, meta_src_path, rem_f_path, add_f_path, meta_f_path):
    """ Split and prevent empty lines to crash the network
    """
    if os.path.isfile(exclude_path):
        out = open(exclude_path, 'r')
        commits = out.read()
        commits_list = commits.split('\n')
    else:
        commits_list = []
    rem = []
    add = []
    met = []
    buffer = 10000
    with open(src_f_path) as src_f:
        with open(add_f_path, 'w') as add_f:
            with open(meta_src_path, 'r') as meta_f:
                with open(meta_f_path, 'w') as meta_out:
                    with open(rem_f_path, 'w') as rem_f:
                        meta = meta_f.readlines()
                        for i, line in enumerate(src_f):
                            if not meta[i].split(',')[0] in commits_list:
                                if len(line) > 0:
                                    rem_line, add_line = line.split('\t')
                                    add_line = add_line.replace('\n', ' ; ')
                                    if "<CTX>" in rem_line:
                                        removed, ctx = rem_line.split("<CTX>")
                                        if len(removed) == 0 or removed.isspace():
                                            continue
                                        if len(ctx.replace('\n', '')) == 0 or ctx.isspace():
                                            ctx = " ; "
                                        rem_line = removed + ' <CTX> ' + ctx
                                    if len(rem_line) == 0 or rem_line.isspace():
                                        continue
                                    rem.append(rem_line)
                                    add.append(add_line)
                                    met.append(meta[i].replace('\n', ''))
                                if i % buffer == buffer - 1:
                                    rem_f.write('\n'.join(rem))
                                    add_f.write('\n'.join(add))
                                    meta_out.write('\n'.join(met))
                                    rem = []
                                    add = []
                                    met = []
                        rem_f.write('\n'.join(rem))
                        add_f.write('\n'.join(add))
                        meta_out.write('\n'.join(met))
