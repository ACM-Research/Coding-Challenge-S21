# ACM Research Coding Challenge (Spring 2021) - Pax Gole
## Citations

I primarily used **Edinburgh Genome Foundry's** "DNA Features Viewer" library for the image.

1. Edinburgh Genome Foundry (2021) **DNA Features Viewer** (Version 3.03). [https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer](https://github.com/Edinburgh-Genome-Foundry/DnaFeaturesViewer)
    `Used the library to create the image.`
2. National Center for Biotechnology Information (2021) **Sample Genbank Record**. [https://www.ncbi.nlm.nih.gov/Sitemap/samplerecord.html](https://www.ncbi.nlm.nih.gov/Sitemap/samplerecord.html)
    `Used the website to understand the genbank.`

Other than that, I used the genbank file provided by ACM UTD and used [https://coolors.co/](https://coolors.co/) for the color palette.

## Solution

I used Python as recommended. I first looked into how I could read and interpret the genbank file and found that the format had been accepted
as the standard by the National Institute of Health's National Center for Biotechnology Information, who also kept a large database of such files
and information on how to read them. I then looked into possible libraries to display the image and found two, the Edinburgh Genome Foundry's
library called "DNA Features Viewer" and Biopython. I ended up choosing DNA Features Viewer. My image file is a PNG named
"TomatoCSVFeaturesCircularGraph".
