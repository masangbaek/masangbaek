N = int(input()) # 5

result =  ""
for i in range(1, N + 1): # i = 1
    for j in range(N, i, -1): # 5 4 3 2 는 공백처리
        result += " "
    for k in range(i): # i = 1 별처리
        result += "*"
    result += "\n" # 줄바꿈 
print(result)
        