# 입력
num = input().split()

# 처리 및 출력
a = int(num[0])
b = int(num[1])
# print(a, b)

if a > b:
    print(">")
elif a < b:
    print("<") 
else:
    print("==")


