from DNAToolkit import *
import random

rndDNAstr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])

print(Nucleotides)

validSTR =validateSeq(rndDNAstr)
print(countNuqFreq(validSTR))