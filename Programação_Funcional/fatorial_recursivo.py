def fatorial(n):
    return n * (fatorial(n-1) if (n-1) > 1 else 1)


n=10
print(f'{n}! = {fatorial(n)}')
