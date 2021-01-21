# Biopython and GenomeDiagram for DNA visualization
##https://biopython.org/wiki/Documentation General docs
##https://biopython.org/docs/1.75/api/Bio.GenBank.html   Read the genbank file
##http://biopython.org/DIST/docs/GenomeDiagram/userguide.pdf Make an image out of the genbank file
# NumPy for math
# http://biopython.org/DIST/docs/tutorial/Tutorial.html
# Installed ReportLab for graphics

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio import GenBank, SeqIO, Graphics
from Bio.Graphics import GenomeDiagram
from numpy import *

gb_data = SeqIO.read("Genome.gb", "genbank")  # Read Genome.gb and store it as a GenBank record

max_len = 0;                    #Find the length of the genome and use it to mark the start/end point
for item in gb_data.features:
    if item.type=="source":
        max_len = item.location.end
        break

circle_diagram = GenomeDiagram.Diagram(gb_data.id)  # Create empty diagram
gene_track = circle_diagram.new_track(0, name="Genes", start=0, end=max_len)  # Create empty track to display genes
gene_set = gene_track.new_set()  # Set of features on track

gene_count = 1



for item in gb_data.features:  # Iterate through each item in the GenBank record object
    if item.type == "gene":
        if gene_count < 0:
            gene_set.add_feature(item, color=colors.blue, label=True, label_size=1.5*cm, label_angle=0, sigil="ARROW", label_position='start', name_qualifiers = item.qualifiers)
        else:
            gene_set.add_feature(item, color=colors.green, label=True, label_size=1.5*cm, label_angle=0, sigil="ARROW", label_position='start')
        gene_count = gene_count * -1

    else:
        continue

circle_diagram.draw(format="circular", circular=True, pagesize=(50 * cm, 50 * cm), start=0, end=len(gb_data), circle_core=.25, track_size=.2)
circle_diagram.write("genome_diagram.png", "PNG")
