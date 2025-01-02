from DNAToolkit import *
import random

rndDNAstr = ''.join([random.choice(Nucleotides)
                    for nuc in range(50)])


validSTR =validateSeq(rndDNAstr)

print(f'\nSequence: {validSTR}\n')
print(f'[1] + Sequence Length: {len(validSTR)}\n')
print (f'[2] + Nucleotide Frequency: {countNuqFreq(validSTR)}\n')

print(f'[3] + DNA/RNA Transcription: {transcription(validSTR)}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {validSTR} 3'")
print(f"   {''.join(['|' for c in range(len(validSTR))])}")
print(f"3' {reverse_complement(validSTR)} 5'\n")
