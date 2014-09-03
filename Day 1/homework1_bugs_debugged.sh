#!/bin/bash

#
echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1

A="SRR072893"
B="SRR072903"
C="SRR072905"
D="SRR072915"

GENOME_DIR=/Users/cmdb/data/genomes
READS="dmel5"
ANNOTATION=dmel-all-r5.57.gff

CORES=4

for THING in $A $B $C $D
do
	echo gunzip $FASTQ_DIR/$THING
	echo fastqc $FASTQ_DIR/$THING
	echo tophat -p4 -o $OUTPUT_DIR/$THING -G $GENOME_DIR/$ANNONTATION  $FASTQ_DIR/$THING
	echo cufflinks -p4 -G $GENOME_DIR/$ANNONTATION $OUTPUT_DIR/$THING/accepted_hits.bam
done


""""/Users/cmdb/cmdb-bootcamp-homework/Day 1 $ ./homework1_bugs_debugged.sh 
There are around 6 mistakes
gunzip /Users/cmdb/data/fastq/SRR072893
fastqc /Users/cmdb/data/fastq/SRR072893
tophat -p4 -o /Users/cmdb/data/day1/SRR072893 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/fastq/SRR072893
cufflinks -p4 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/day1/SRR072893/accepted_hits.bam
gunzip /Users/cmdb/data/fastq/SRR072903
fastqc /Users/cmdb/data/fastq/SRR072903
tophat -p4 -o /Users/cmdb/data/day1/SRR072903 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/fastq/SRR072903
cufflinks -p4 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/day1/SRR072903/accepted_hits.bam
gunzip /Users/cmdb/data/fastq/SRR072905
fastqc /Users/cmdb/data/fastq/SRR072905
tophat -p4 -o /Users/cmdb/data/day1/SRR072905 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/fastq/SRR072905
cufflinks -p4 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/day1/SRR072905/accepted_hits.bam
gunzip /Users/cmdb/data/fastq/SRR072915
fastqc /Users/cmdb/data/fastq/SRR072915
tophat -p4 -o /Users/cmdb/data/day1/SRR072915 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/fastq/SRR072915
cufflinks -p4 -G /Users/cmdb/data/genomes/ /Users/cmdb/data/day1/SRR072915/accepted_hits.bam""""