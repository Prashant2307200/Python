def sum(n):
    if(n == 0 or n == 1):
        return n;
    return n + sum(n-1)

print(sum(5))