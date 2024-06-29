N = int(input()) # 5

result = "" # 결과 저장
for i in range(1, N + 1): # 1부터 5까지
    for j in range(N, i- 1, -1): # range(5, 0, -1) : 5 4 3 2 1
        result += "*" # 5 4 3 2 1 을 * 로 result에 넣어주자
    result += "\n" # 5 줄바꿈 4 줄바꿈, ... 
print(result) # 출력