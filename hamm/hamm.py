"""rosalind answer"""

file: str = "/rosalind_hamm.txt"

def hamm(file: str) -> int:
    #initialize
    s: str = ''
    t: str = ''
    hammdist: int = 0
    i = 0
    #read file
    s,t = open(file).read().split()
    while i < len(s) - 1:
        if s[i] != t[i]:
            hammdist += 1
        i +=1
    return(hammdist)

print(hamm(file))