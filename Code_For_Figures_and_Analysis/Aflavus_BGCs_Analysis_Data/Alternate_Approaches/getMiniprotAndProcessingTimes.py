import os
import sys

import statistics

def parseTime(xstring):
    xs = xstring.split(':')
    hour = float(xs[0])
    minute = float(xs[1])/60.0
    return(hour + minute)

preptg_progress_log_file = 'prepTG_DB/Progress.log'

sample_start_times = {}
sample_end_times = {}
with open(preptg_progress_log_file) as opplf:
    for line in opplf:
        line = line.strip()
        ls = line.split()
        if 'miniprot -t1 -d' in line:
            if 'Running' in line:
                sample = ls[12].split('/')[-1].split('.mpi')[0]
                time = parseTime(ls[1])
                sample_start_times[sample] = time
            else:
                sample = ls[10].split('/')[-1].split('.mpi')[0]
                time = parseTime(ls[1])
                sample_end_times[sample] = time

time_diffs = []
for sample in sample_start_times:
    time_diff = sample_end_times[sample] - sample_start_times[sample]
    #print(sample + '\t' + str(time_diff))
    time_diffs.append(time_diff)

print(statistics.mean(time_diffs))
