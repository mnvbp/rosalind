"""rosalind answer"""

#The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months
#produce a single pair of offspring

def fibd(month, life) -> list:
    #initialize matrix
    matrix = [[0 for x in range(life)] for y in range(month)] 
    matrix[0][0] = 1
    #iterate through every generation
    for i in range(0, month):
        #promoter
        for z in range(0, life):
            matrix[i][z] += matrix[i-1][z-1]
        #births
        for z in range(1, life - 1):
            matrix[i][0] += matrix[i-1][z]
    answer = sum(matrix[month-1])
    return answer


#top answer
def fib(n,k=1):
  ages = [1] + [0]*(k-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
    #print(ages)
  return sum(ages)
