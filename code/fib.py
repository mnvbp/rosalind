
def reccur(n: int, k: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return k
    if n <= 4:
        return (reccur(n-1,k) + reccur(n-2, k))
    num = reccur(n-1,k) + k * reccur(n-2, k)
    return num
