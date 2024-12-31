from DNAToolkit import *
import random

rndDNAstr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])

print(validateSeq(rndDNAstr))