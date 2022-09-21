import os
import argparse
import pandas as pd 
from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio import SeqIO



parser = argparse.ArgumentParser(prog="standard.py", formatter_class=argparse.RawTextHelpFormatter, description="""\n""",epilog="""
    Examples:
    python3 standard.py -s rawsequence.fastq\n""")
parser.add_argument('--sequence', '-s', type=str, default="", required=True, help='Raw sequence file in FASTQ format.')
args = parser.parse_args()
file_name =  args.sequence
file_title = file_name.split(".")
if file_title[1] != 'fastq':
	sys.exit('Please provide a FASTQ file')

file_input = file_title[0]

os.system("mkdir additional_files")
os.system("mkdir Final_result")

in_seq = "seqtk seq -a {}.fastq > additional_files/test1.fasta".format(file_input)
os.system(in_seq)

os.system("seqtk seq -L 1000 additional_files/test1.fasta > additional_files/test_large_seq.fasta")
os.system("blastn -query additional_files/test_large_seq.fasta -db database/zymo -out additional_files/query_pathogen_final.csv -outfmt 6 -evalue 1e-100 -max_target_seqs 10 -perc_identity 85 -qcov_hsp_perc 95 -task megablast")
df = pd.read_csv("additional_files/query_pathogen_final.csv", sep = "\t", names = ['query' , 'subject', 'identity', "Alignment lenth", "mismatches", "gap opens", "qstart", "qend", "s start", "s end", "evalue", "bitscore"])
#print(df)

df['subject'] = df['subject'].apply(lambda x: ' '.join(x.split('_')[1:3]))
df = df.sort_values('query').drop_duplicates(subset=['query', 'subject'])
total = df['subject'].value_counts()
total.to_csv('additional_files/pathogen_final_result.csv')
#print(total)

df2 = pd.read_csv('additional_files/pathogen_final_result.csv', names = ['Organism', 'HITS'])
df2 = df2.iloc[1:]
df2['Relative Abundance(%)'] = (df2['HITS'].astype(float) / df2['HITS'].astype(float).sum()) * 100 
df2.to_csv('Final_result/final_result.csv')
print(df2['HITS'].astype(float).sum())
print(df2)

