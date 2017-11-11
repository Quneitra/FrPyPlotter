#!/usr/bin/env python3

import matplotlib
matplotlib.use('Agg')
import argparse
import re
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser("FRPylotter V.0.5 10/12/2017\t Script to plot fragment recruitment plots")
parser.add_argument("-s", "--source", help="Source file")
parser.add_argument("-f", "--fltype", help="Filetype[1/2], 1: FR-HIT, 2:BLAST+ tabular", type=int)
parser.add_argument("-t", "--title", help="Bacterial refgenome name")
parser.add_argument("-o", "--out", help="Output file name")
arg = parser.parse_args()

tl = arg.title
flswch = arg.fltype
out = arg.out
pi = []
ps = []
ctr = 0
ftype = ''

ifl = open(arg.source)
for line in ifl:
    ctr+=1
    data = line.split()
    if flswch == 1:
        ftype = "FR-HIT"
        pid = data[7].rstrip("%")
        pi.append(float(pid))
        pos = int(data[9])
        ps.append(pos)
    else:
        ftype = "BLASTN"
        pid = data[2]
        pi.append(float(pid))
        ln.append(int(data[3]))
        pos = int(data[8])
        ps.append(pos)


print(ctr)
plt.xlabel("Position in genome (bp)")
plt.ylabel("% Identity")
plt.xlim(0, np.max(ps) + 1)
plt.ylim(0, 100)
for i in range(0, len(pi)):
    plt.plot(ps[i], pi[i], 'go', ms=1, alpha=0.5)
plt.title("{0}({1}), {2} reads".format(str(tl), str(ftype), str(ctr)))
plt.savefig(out)