"translate rna into protein"

file: str = '/rosalind_prot.txt'

codon_table: dict = {'UUU':'F','CUU':'L','AUU':'I','GUU':'V',
                     'UUC':'F','CUC':'L','AUC':'I','GUC':'V',
                     'UUA':'L','CUA':'L','AUA':'I','GUA':'V',
                     'UUG':'L','CUG':'L','AUG':'M','GUG':'V',
                     'UCU':'S','CCU':'P','ACU':'T','GCU':'A',
                    'UCC':'S','CCC':'P','ACC':'T','GCC':'A',
                    'UCA':'S','CCA':'P','ACA':'T','GCA':'A',
                    'UCG':'S','CCG':'P','ACG':'T','GCG':'A',
                    'UAU':'Y','CAU':'H','AAU':'N','GAU':'D',
                    'UAC':'Y','CAC':'H','AAC':'N','GAC':'D',
                    'UAA':'Stop','CAA':'Q','AAA':'K','GAA':'E',
                    'UAG':'Stop','CAG':'Q','AAG':'K','GAG':'E',
                    'UGU':'C','CGU':'R','AGU':'S','GGU':'G',
                    'UGC':'C','CGC':'R','AGC':'S','GGC':'G',
                    'UGA':'Stop','CGA':'R','AGA':'R','GGA':'G',
                    'UGG':'W','CGG':'R','AGG':'R','GGG':'G'}


def get_prot(file: str) -> str:
    protein_string = ''
    protein = ''
    codon = ''
    with open(file, 'r') as infile:
        for line in infile:
            for letter in line:
                codon = codon + letter
                if len(codon) == 3:
                    protein = codon_table[codon]
                    if protein == 'Stop':
                        return(protein_string)
                    else:
                        protein_string = protein_string + protein
                        codon = ''

print(get_prot(input))