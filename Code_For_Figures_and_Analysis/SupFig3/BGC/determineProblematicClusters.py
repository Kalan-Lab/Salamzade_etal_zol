import os 
import sys

resdir = 'zol_fai_param_selections/'
for c in os.listdir(resdir):
    resfile = resdir + c + '/Parameter_Recommendations_for_fai.txt'
    if not os.path.isfile(resfile):
        print(c)

