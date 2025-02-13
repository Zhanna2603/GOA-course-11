"""https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python"""

# Complementary DNA

def DNA_strand(dna):
    if 'A' in dna:
        dna = dna.replace('A', 'B')
    if 'T' in dna:
        dna = dna.replace('T', 'A')
    if 'B' in dna:
        dna = dna.replace('B', 'T')
    if 'C' in dna:
        dna = dna.replace('C', 'D')
    if 'G' in dna:
        dna = dna.replace('G', 'C')
    if 'D' in dna:
        dna = dna.replace('D', 'G')
    return dna