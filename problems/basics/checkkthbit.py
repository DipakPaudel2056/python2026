def kthbit(n,k):
    return (n>>k) & 1 == 1

print(kthbit(4,0))
