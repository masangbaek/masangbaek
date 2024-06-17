# 입력
t_score = int(input())

# 처리 및 출력 
if 90 <= t_score <= 100:
    print("A")
elif 80<= t_score <= 89:
    print("B")
elif 70<= t_score <= 79:
    print("C")
elif 60<= t_score <= 69:
    print("D")
else:
    print("F")