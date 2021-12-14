# nanopore_standard_read
In house script for determining constituent of zymo standard using nanopore read

Prerequisites:

BLAST+:

`sudo apt-get update`

`sudo apt-get install ncbi-blast+-legacy`

seqtk:

`sudo apt-get install seqtk`


porechop:

`sudo apt-get install porechop`



Python dependencies:

`pip3 install pandas`
`pip3 install biopython`

Download the database(https://drive.google.com/drive/folders/1rDwvenlss02S9Y_TfceOKQjduQG4IJVn?usp=sharing) files and put in the database folder.

`usage: standard.py [-h] --sequence SEQUENCE

optional arguments:
  -h, --help            show this help message and exit
  --sequence SEQUENCE, -s SEQUENCE
                        Raw sequence file in FASTQ format.

    Examples:
    python3 standard.py -s rawsequence.fastq`
