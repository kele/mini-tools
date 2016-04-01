#!/usr/bin/env python3

from multiprocessing import Pool
import subprocess

import os
import sys

maindir = sys.argv[1]
command = sys.argv[2]

def run(filename):
    os.system("{cmd} {fullpath} > {fullpath}_OUT".format(cmd=command,
                                                         fullpath=maindir + "/" + filename))

files = os.listdir(maindir)

with Pool(processes=8) as pool:
    print("Running {}".format(command))
    pool.map(run, files)
    pool.close()
    pool.join()

