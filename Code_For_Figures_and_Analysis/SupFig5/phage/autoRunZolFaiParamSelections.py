import os
import sys

in_dir = os.path.abspath(sys.argv[1]) + '/'
res_dir = os.path.abspath('zol_fai_param_selections/') + '/'

if not os.path.isdir(res_dir):
    os.system('mkdir ' + res_dir)

for c in os.listdir(in_dir):
    res = res_dir + c + '/'
    cmd = ['zol', '-i', in_dir + c + '/', '-o', res, '-sfp', '-c', '20', '--rename_lt']
    os.system(' '.join(cmd))
