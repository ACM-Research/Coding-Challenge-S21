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


circle_diagram = GenomeDiagram.Diagram(gb_data.id)  # Create empty diagram
gene_track = circle_diagram.new_track(0, name="Genes")  # Create empty track to display genes
gene_set = gene_track.new_set()  # Set of features on track
cds_track = circle_diagram.new_track(1, name="Coding Regions")
cds_set = cds_track.new_set()

gene_count = 1
cds_count = 1


for item in gb_data.features:  # Iterate through each item in the GenBank record object
    print(item)
    if item.type == "gene":
        if gene_count < 0:
            gene_set.add_feature(item, color=colors.blue, label=True, label_size=20, label_angle=0)
        else:
            gene_set.add_feature(item, color=colors.green, label=True, label_size=20, label_angle=0)
        gene_count = gene_count * -1

    elif item.type == "CDS":
        if cds_count < 0:
            cds_set.add_feature(item, color=colors.red, label=True, label_size=30, label_angle=90)
        else:
            cds_set.add_feature(item, color=colors.black, label=True, label_size=30, label_angle=90)
        cds_count = cds_count * -1

    else:
        continue






circle_diagram.draw(format="circular", circular=True, pagesize=(50 * cm, 50 * cm), start=0, end=len(gb_data), circle_core=.25, track_size=.2)
circle_diagram.write("genome_diagram.png", "PNG")
