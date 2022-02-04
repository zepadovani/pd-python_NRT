#!/usr/bin/env python3

import os
import subprocess
import random
from multiprocessing import Pool

path = os.getcwd()
os.chdir(path)

def synth(i):
    fr = random.uniform(220, 880)
    dr = random.randrange(1, 10) * 500

    filename = f'{i+1:02}' + '-sine-fr_' + str(round(fr,2)) + '-dur_' + str(dr) + '.wav'

#   command below assumes that pd is in your environment variables... change to the correct path if needed
    cmd = r'pd -nogui -open pd_abs_NRT.pd -send "nrt name ' + filename + ', freq ' + str(round(fr,6)) + ', dur ' + str(dr) + '"'

    subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).stdout.read()

if __name__ == '__main__':
    with Pool(processes=8) as pool:
        pool.map(synth, list(range(50)))
