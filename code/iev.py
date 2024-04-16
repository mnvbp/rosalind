"""rosalind answer"""

#number of children from each pair
CHILDREN: int = 2


#AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
sample: str = [16996, 18555, 19374, 17197, 19343, 16522]
#weights for children displaying dominant
weights: list = [1, 1, 1, .75, .5, 0]

count = 0
for i in zip(sample, weights):
    ev = i[0] * i[1] * CHILDREN
    count += ev

print(count)