#!/usr/bin/env python


"""
Parse a single FASTA record from stdin and print it
"""

###### want to make a program that parses out multiple FASTA files... must be able to keep track of what its doing

import sys

from fasta import FASTAReader

reader = FASTAReader( sys.stdin )

all_seqs = []   #take seqs outputs from module and placed them in a list
for sid, sequence in reader:
    all_seqs.append(sequence)

sort_seqs = sorted(all_seqs, key = len, reverse = True)

top_hundo = sort_seqs[0:100]

"""
rev_top_hundo = []   #when i print this, its empty....
for rev_top_hundo in top_hundo:
    def complement(s): 
        basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', ' ' : ' ', ',' : ',', '[' : '[', ']' : ']'} 
        letters = list(s) 
        letters = [basecomplement[base] for base in letters] 
        return ''.join(letters)
    def revcom(s):
        return complement(s[::-1])
    #####print(rev_top_hundo)   #returns original, no good
    #####print(complement(rev_top_hundo[::-1]))  ### good returns same as below
#    print(revcom(rev_top_hundo))  ####gives each strand reversed from original in correct order, with each starting on a new line
        return (revcom(rev_top_hundo))
    reverse_compliments = (revcom(rev_top_hundo))     #now i have the reverse compliments saved as a variable
   # print reverse_compliments
"""


def complement(s): 
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', ' ' : ' ', ',' : ',', '[' : '[', ']' : ']'} 
    letters = list(s) 
    letters = [basecomplement[base] for base in letters] 
    return ''.join(letters)
#def revcom(s):
#    return complement(s[::-1])
#####print(rev_top_hundo)   #returns original, no good
#####print(complement(rev_top_hundo[::-1]))  ### good returns same as below
#    print(revcom(rev_top_hundo))  ####gives each strand reversed from original in correct order, with each starting on a new line
#    return (revcom(rev_top_hundo))

rev_top_hundo = []
for things in top_hundo:
    x = complement(things)
    reverse_complement = x[::-1]
    rev_top_hundo.append(reverse_complement)
print rev_top_hundo



"""
rev_rev_top_hundo = []
for rev_rev_top_hundo in reverse_compliments:
    def complement(s): 
        basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', ' ' : ' ', ',' : ',', '[' : '[', ']' : ']'} 
        letters = list(s) 
        letters = [basecomplement[base] for base in letters] 
        return ''.join(letters)
    def revcom(s):
        return complement(s[::-1])
    #####print(rev_top_hundo)   #returns original, no good
    #####print(complement(rev_top_hundo[::-1]))  ### good returns same as below
#    print(revcom(rev_top_hundo))  ####gives each strand reversed from original in correct order, with each starting on a new line
        return (revcom(rev_rev_top_hundo))
    top_hundo_convert = (revcom(rev_rev_top_hundo))
    print top_hundo_convert
"""




    
"""
Convert orginal sequence to match format of new reverse compliment (), will run reverse compliment back thru revcom program
"""

#converted_top_hundo = []
#for converted_top_hundo in rev_top_hundo:
#    def complement(s): 
#        basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', ' ' : ' ', ',' : ',', '[' : '[', ']' : ']'} 
#        letters = list(s) 
#        letters = [basecomplement[base] for base in letters] 
#        return ''.join(letters)
#    def revcom(s):
#        return complement(s[::-1])
#    print(revcom(rev_top_hundo))


"""
Tryed ifferent ways to get revrerse comp... 

#def ReverseComplement1(top_hundo):
#    seq_dict = {'A':'T','T':'A','G':'C','C':'G'}
#    return "".join([seq_dict[base] for base in reversed(seq)])
#    print "".join([seq_dict[base] for base in reversed(seq)])
    
    
#revcomp_top_hundo = ReverseComplement1(top_hundo)

#print revcomp_top_hundo


### try to make reverse comp a module and then call it here and run it here and put into txt file


#print all_seqs    
#print type(all_seqs) ### list with all the seqs (strings) sepparated by coma


#print sorted(all_seqs)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#print sort_seqs
#from revcompl import RevStrCompiler

#revcompl = lambda x: ''.join([{'A':'T','C':'G','G':'C','T':'A'}[B] for B in x][::-1])

#print revcompl(top_hundo)
"""
