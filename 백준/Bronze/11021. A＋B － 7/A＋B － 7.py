T = int(input())

for n in range(1, T + 1):
    sum_ = sum(map(int, input().split()))
    print(f"Case #{str(n)}: {sum_}")