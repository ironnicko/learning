n = int(input('Enter the limit:'))
print(*[i for i in range(1, n + 1)])
for i in range(n - 1, 1, -1):
    print(f' '*(2*(i-1)) + f'{i}')
print(*[i for i in range(1, n+1)])
