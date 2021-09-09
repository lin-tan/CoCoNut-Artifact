import sys

src_f_path, rem_f_path, add_f_path, src_meta, out_meta = sys.argv[1:]
rem = []
add = []
met = []
buffer = 20000
with open(src_f_path) as src_f:
    with open(out_meta, 'w') as out_f:
        with open(src_meta) as src_meta:
            meta_lines = src_meta.readlines()
            print(len(meta_lines))
            with open(add_f_path, 'w') as add_f:
                with open(rem_f_path, 'w') as rem_f:
                    for i, line in enumerate(src_f):
                        if len(line) > 0:
                            rem_line, add_line = line.split('\t')
                            add_line = add_line.replace('\n','')
                            if "<CTX>" in rem_line:
                                removed, ctx = rem_line.split("<CTX>")
                                if len(removed) == 0 or removed.isspace():
                                    removed = "<EMPTY>"
                                if len(ctx.replace('\n', '')) == 0 or ctx.isspace():
                                    ctx = "<EMPTY>"
                                rem_line = removed + ' <CTX> ' + ctx
                            if len(rem_line) == 0 or rem_line.isspace():
                                continue
                            elif rem_line.startswith("import") or rem_line.startswith("package"):
                                continue
                                
                            elif rem_line.startswith("//") and add_line.startswith("//"):
                                continue
                            
                            elif rem_line == add_line:
                                continue
                            else:

                                rem.append(rem_line)
                                add.append(add_line)
                                met.append(meta_lines[i])
							
                        if i%buffer == buffer-1:
                            
                            rem_f.write('\n'.join(rem))
                            add_f.write('\n'.join(add))
                            out_f.write(''.join(met))
                            rem = []
                            add = []
                            met = []
                    assert(len(rem) == len(met))
                    print(len(rem))
                    print(len(add))
                    print(len(met))
                    rem_f.write('\n'.join(rem))
                    add_f.write('\n'.join(add))
                    out_f.write(''.join(met))
