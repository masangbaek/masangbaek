N = int(input()) # 5

result = ''
for i in range(N, 0, -1): # i = 5 
    for j in range(N - i): # j = 0
        result += " "
    for k in range(2 * i - 1): # k = 9
        result += "*"
    result += "\n"
print(result)