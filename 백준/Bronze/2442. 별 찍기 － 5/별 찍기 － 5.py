N = int(input()) # 5

result = ""
for i in range(1, N + 1): # 1 2 3 4 5
    for j in range(N, i, -1): # 5 4 3 2 1 
        result += " " # j 5일 경우 공백 5칸
    for k in range(0, 2 * i - 1):
        result += "*" # i가 1일 경우 0번 위치에 * 
    result += "\n"
print(result)