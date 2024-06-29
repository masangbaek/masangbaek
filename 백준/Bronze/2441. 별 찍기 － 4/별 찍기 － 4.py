N = int(input())

result = ""
for i in range(1, N + 1): # 각 줄
    # 각 줄의 앞에 들어갈 공백의 개수 (i - 1)
    result += " " * (i -1)
    # 각 줄의 별의 개수는 (N - i + 1)
    result += "*" * (N - i + 1)
    result += "\n"
print(result)