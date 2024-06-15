# 2회차 

# 입력
raw_num = input().split() # 한 줄에 입력후 공백 기준으로 분리해줍니다. ['1', '2']
# print(raw_num)

# 처리 

a_num = raw_num[0] # 첫번째 인덱스 1
b_num = raw_num[1] # 두번째 인덱스 2
# print(a_num, b_num, type(a_num), type(b_num))

a = int(a_num) # 1
b = int(b_num) # 2
# print(a, b, type(a), type(b))

# 출력
print(a + b)