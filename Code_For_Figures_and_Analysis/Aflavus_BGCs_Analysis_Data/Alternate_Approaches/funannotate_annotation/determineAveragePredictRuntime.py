import os
import sys
import statistics

def parseTime(xstring):
    xs = xstring.split(':')
    hour = float(xs[0])
    minute = float(xs[1])/60.0
    return(hour + minute)

fundir = 'funannotate_Results/'
all_times = []
for s in os.listdir(fundir):
    log_file = fundir + s + '/gene_prediction_results/logfiles/funannotate-predict.log'
    count = 0
    first_time = None
    last_time = None
    with open(log_file) as olf:
        for line in olf:
            line = line.strip()
            if not line.startswith('['): continue
            ls = line.split()
            time = parseTime(ls[1][:-2])
            if count == 0:
                first_time = time
            count += 1
            last_time = time

    time_diff = last_time - first_time
    if time_diff < 0:
        time_diff = (24.0-first_time) + last_time
    
    #print(s + '\t' + str(time_diff))
    all_times.append(time_diff)

print(statistics.mean(all_times))
