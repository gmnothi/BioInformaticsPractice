# DNA Toolkit File

Nucleotides = ["A", "C", "G","T"]

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