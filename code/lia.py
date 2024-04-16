"""rosalind answer"""

def lia(k: int, n: int) -> float:
    # calculate factorial for binomial
    def factorial(fact: int) -> int:
        if fact == 0:
            return 1
        for i in range(1, fact):
            fact *= i
        return fact
    # initialize values and calculate population
    gen = 2**k
    summ = 0
    # calculate binomial in (inclusive) range n to gen and sum together
    for i in range(n, gen + 1):
        ncr = factorial(gen)/(factorial(i) * factorial(gen-i))
        # all combinations of genotypes with AaBb punnet has .25 chance of AaBb (.5 each allele)
        binom = (.25**i) * (.75 ** (gen - i))
        summ += (binom * ncr)
    return summ

print(lia(5, 8))