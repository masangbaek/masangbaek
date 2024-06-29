N = int(input())

factorial = 1 # 곱셈의 항등원 결과를 바꾸지 않음
for i in range(N, 0, -1): # N부터 역반복
    factorial *= i # 곱해준다

print(factorial)