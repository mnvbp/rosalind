"""rosalind answer"""


file: str = '/rosalind_mrna.txt'


def mrna(file: str) -> int:
    proteins: dict = {'F': 2, 'L': 6, 'I': 3, 'V': 4, 'M': 1, 
                  'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2, 
                  'H': 2, 'N': 2, 'D': 2, 'Stop': 3, 'Q': 2, 
                  'K': 2, 'E': 2, 'C': 2, 'R': 6, 'G': 4, 
                  'W': 1}
    STOP: int = 3
    answer: int = 1
    prot: list = list(open(file).read().rstrip())
    for letter in prot: 
        answer *= proteins[letter]
    answer = answer * STOP % 1000000
    return(answer)


print(mrna(file))



#initial converter
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
test: list = list(codon_table.values())
prot_num: dict = {}
for key in test:
    num = test.count(key)
    prot_num[f'{key}'] = num


