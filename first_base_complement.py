>>> dna="AGCTGCACGTACG"
>>> basecomplement={'A':'T','G':'C','T':'A','C':'G','N':'N','a':'t','g':'c','t':'a','c':'g','n':'n'}
>>> letters=list(dna)
>>> letters
['A', 'G', 'C', 'T', 'G', 'C', 'A', 'C', 'G', 'T', 'A', 'C', 'G']
>>> letters=[basecomplement[base] for base in letters]
>>> letters
['T', 'C', 'G', 'A', 'C', 'G', 'T', 'G', 'C', 'A', 'T', 'G', 'C']
