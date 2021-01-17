#Biopython and GenomeDiagram for DNA visualization
##https://biopython.org/wiki/Documentation General docs
##https://biopython.org/docs/1.75/api/Bio.GenBank.html   Read the genbank file
##http://biopython.org/DIST/docs/GenomeDiagram/userguide.pdf Make an image out of the genbank file
#NumPy for math
#http://biopython.org/DIST/docs/tutorial/Tutorial.html
#Installed ReportLab for graphics

from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio import GenBank, SeqIO, Graphics
from Bio.Graphics import GenomeDiagram
from numpy import *


gb_data = SeqIO.read("Genome.gb", "genbank")
print(gb_data.seq)

circle_diagram = GenomeDiagram.Diagram(gb_data.id)
diagram_track = circle_diagram.new_track(1, name="Annotated Features")
diagram_item_set = diagram_track.new_set()

for item in gb_data.features:
    if item.type != "gene":
        continue
    if len(diagram_item_set) % 2 == 0:
        color = colors.black
    else:
        color = colors.green

    diagram_item_set.add_feature(item, color=color, label=True)

circle_diagram.draw(format="circular", circular=True, pagesize = (50 * cm, 50 * cm), start = 0, end = len(gb_data))
circle_diagram.write("genome_diagram.png", "PNG")
