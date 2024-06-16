# 입력
n_1 = input() # (1)의 위치에 들어갈 세 자리 자연수 472
n_2 = input() # (2)의 위치에 들어갈 세 자리 자연수 385
# print(n_1, n_2)

# 처리 
a = n_1[0:3]
b = n_2[2]
# print(a, b)
int(a)
int(b)

a1 = n_1[0:3]
b1 = n_2[1]
int(a1)
int(b1)

a2 = n_1[0:3]
b2 = n_2[0]
int(a2)
int(b2)

a3 = n_1[0:3]
b3 = n_2[0:3]
int(a3)
int(b3)

# 출력
print(int(a) * int(b)) # 2360
print(int(a1) * int(b1)) # 3776
print(int(a2) * int(b2)) # 1416 
print(int(a3) * int(b3)) # 472 * 385 181720
