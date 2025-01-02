# DNA Toolkit File
import collections
from sequences import *


def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNuqFreq(seq):
    tmpFreqDict = {"A":0,  "C":0, "G":0, "T":0}
    for nuq in seq:
        tmpFreqDict[nuq] += 1
    return tmpFreqDict

def transcription(seq):
    return seq.replace("T", "U")

def reverse_complement(seq):
    return ''.join([DNA_ReverseComp[nuc] for nuc in seq])[::-1]