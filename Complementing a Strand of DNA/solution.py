# s = input()

# # V.1
# def reverse_complement(s):
#   s_reversed = s[::-1]
#   sc = s_reversed.replace('A', '%temp%').replace('T', 'A').replace('%temp%', 'T').replace('G', '%var%').replace('C', 'G').replace('%var%', 'C')
#   return sc

# print(reverse_complement(s))


# V.2
# s = s.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
# print(s)

# V.3
# print(s[::-1].translate(str.maketrans('ACGT', 'TGCA')))
