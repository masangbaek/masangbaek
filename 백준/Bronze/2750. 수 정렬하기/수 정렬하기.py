result = set() # set으로 중복제거 
N = int(input()) # 수의 개수
    
for i in range(N): # 줄의 개수 반복
    result.add(int(input()))
    
result = sorted(result)

for i in result:
    print(i)