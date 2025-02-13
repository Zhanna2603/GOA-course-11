"""https://www.codewars.com/kata/5556282156230d0e5e000089/train/python"""

# DNA to RNA Conversion

def dna_to_rna(dna):
    rna = ""
    for nucleotide in dna:
        if nucleotide == 'T':
            rna += 'U'
        else:
            rna += nucleotide
    return rna