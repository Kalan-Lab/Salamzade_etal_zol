import os
import sys
import json

fubar_json_result = sys.argv[1]

fubar_results = None
with open(fubar_json_result) as ofjr:
    fubar_results = json.load(ofjr)

print('x\ty\txend\tyend')
for partition in fubar_results['MLE']['content']:
    i = 1
    for site_mle_info in fubar_results['MLE']['content'][partition]:
        alpha, beta, diff, prob_agb, prob_alb, bayesfactor, _, _ = site_mle_info
        if prob_agb >= 0.9:
            print(str(i) + '\t0\t' + str(i+2) + '\t1')
        i += 3
