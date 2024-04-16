"""substring question"""

file = '/Users/manavparikh/Downloads/rosalind_subs(2).txt'



def subs(file) -> list:
    #initialize variables
    string: str =  ""
    motif: str = ""
    string_list: list = []
    #get file
    string, motif = open(file).read().split()
    #get index
    j: int = 0
    while j < len(string) - 1:
        k = j + len(motif)
        check = string[j:k]
        if check == motif:
            string_list.append(j)
        j += 1
    #base 1 index
    result: list = []
    result_string: str = ""
    for number in string_list:
        result.append(number + 1)
    for number in result:
        result_string += str(number) + " "
    return result_string

print(subs(file))