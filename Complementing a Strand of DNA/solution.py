# s = 'CTCAGCTCGACTTAGGTTACGGGGGAGTCCAATTATGCTGGAGATGCTCTTCAGAGCATTCGTTTCGCTTTCACGAGTTGTTAGGCATATCGGCCGACGCCACGCTACTGCCCCCGAGCGACCCATAGATTCCTGTCCGATCGTTGGGCCCCTTCGTTACTTACTGGGCGCCTCGGCGCCAGCAGAGCCCGCGGGGATTCCCGTTCGTTATGCGTCATACCCATTGGGTTGATATTCATGAATCAGCGCCATCAACTCCACGCAGAACCCGAGTGTTTAGTGTGCCGACGCGCGCGGGACTAGGAGGAATGGGTTACGCTTTTAAGTGGAATCATGTTCCTCACACCGTGTCTGGAGTACCTTGCGCTCAGGTACGCGACTGCCTGCGCCCCAGCGCTCAGCGTGTTAGGTCCTTTGTACCTTTAGACCCACCCGCAGTACATCCGTGGTGCGCAGTCAACTGGATCCGTGATTAAGGATTCCGCGTATACGCTGTTTTGATCAGTATAGATGTCAGGACAGCCTGGCTATGTGGAATGGCGCTACCTGGTTCCTTCTGGGCGCTGTGCAGTTACTAACTGTATCATAACTACCCTGTGAGTTACATGACGCCCCTTAACGTTGCCATACCTCCACCCACGTTCCTTGACGGCGCTGACTCGCCGCTGCCTACGCTCCAATAAACGCGTTATCTCGCCATCGTATGGTTCAGTCAAACCGAGATTTGTTGCGAGTACCATAGGTTCTATGGGTCGAAACCGACGCTAGTCCGCGGATGAATTGGGAGCAGGAACTTTGCACGGGTATCTGCAGGCCAATAGATCCAAAACAGACAGGCATGGAGTAAGCAAGTGGGGTCTCTCTCTTGTTATATGTCAGTGTAAA'

# #  My solution
# def reverse_complement(s):
#   s_reversed = s[::-1]
#   sc = s_reversed.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T').replace('G', '%var%').replace('C', 'G').replace('%var%', 'C')
#   return sc

# print(reverse_complement(s))

#  other solutions
# V.1
# st = "AAAACCCGGT"
# st = st.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# print (st)

# V.2
# s = 'AAAACCCGGT'
# print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))