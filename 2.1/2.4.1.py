
in_file = '../tmp/dataset_24465_4.txt'
out_file = '../tmp/out.txt'
with open(in_file, 'r') as in_f, open(out_file, 'w') as out_f:
    lines = in_f.readlines()
    lines.reverse()
    out_f.writelines(lines)


