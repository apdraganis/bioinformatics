#  (hard code?) a dictionary for RNA codon table
#  loop through the given RNA string
#  every 3 characters, check in the dictionary for key-value pair.

rna_codon_dict = {
  "UUU": "F",      "CUU": "L",      "AUU": "I",      "GUU": "V",
  "UUC": "F",      "CUC": "L",      "AUC": "I",      "GUC": "V",
  "UUA": "L",      "CUA": "L",      "AUA": "I",      "GUA": "V",
  "UUG": "L",      "CUG": "L",      "AUG": "M",      "GUG": "V",
  "UCU": "S",      "CCU": "P",      "ACU": "T",      "GCU": "A",
  "UCC": "S",      "CCC": "P",      "ACC": "T",      "GCC": "A",
  "UCA": "S",      "CCA": "P",      "ACA": "T",      "GCA": "A",
  "UCG": "S",      "CCG": "P",      "ACG": "T",      "GCG": "A",
  "UAU": "Y",      "CAU": "H",      "AAU": "N",      "GAU": "D",
  "UAC": "Y",      "CAC": "H",      "AAC": "N",      "GAC": "D",
  "UAA": "Stop",   "CAA": "Q",      "AAA": "K",      "GAA": "E",
  "UAG": "Stop",   "CAG": "Q",      "AAG": "K",      "GAG": "E",
  "UGU": "C",      "CGU": "R",      "AGU": "S",      "GGU": "G",
  "UGC": "C",      "CGC": "R",      "AGC": "S",      "GGC": "G",
  "UGA": "Stop",   "CGA": "R",      "AGA": "R",      "GGA": "G",
  "UGG": "W",      "CGG": "R",      "AGG": "R",      "GGG": "G" 
}


s = input()


def translate_rna_into_protein(s):
  for i in range(0, len(s), 3):
    codon = s[i:i+3]
    if codon == "UAA" or codon == "UAG" or codon == "UGA":
      break
    else:
      print(rna_codon_dict[codon], end="")

translate_rna_into_protein(s)