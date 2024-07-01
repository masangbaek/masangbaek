T = int(input())

for n in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"Case #{str(n)}: {a} + {b} = {a + b}")