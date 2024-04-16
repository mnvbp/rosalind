"""rosalind answer"""

file: str = '/rosalind_grph.txt'

def grph(file: str) -> str:
    infile = list(open(file).read().split())
    key = ''
    seq = ''
    b = []
    for item in infile:
        if item[0] == '>':
            if key != '':
                b.append(key)
                b.append(seq)
                key = ''
                seq = ''
            else:
                key = item
        else:
            seq += item
    place: str = 0
    for item1 in b:
        if item[0] == '>':
            break
        else:
            place = item1[0:3]
            for item2 in b:
                if place == item2[len(item2-4):len(item2-1)]:
                    print(item1, item2)
        
        
        


grph(file)