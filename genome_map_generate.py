#Biopython and GenomeDiagram for DNA visualization
##https://biopython.org/wiki/Documentation General docs
##https://biopython.org/docs/1.75/api/Bio.GenBank.html   Read the genbank file
##http://biopython.org/DIST/docs/GenomeDiagram/userguide.pdf Make an image out of the genbank file
#NumPy for math
from Bio import GenBank


from numpy import *

with open('Genome.gb') as file:
    print(file.read())
    assert not file.read()
    file.seek(0)
    assert file.read()
