# 입력
H, M = map(int, input().split())

# 처리 및 출력
if 0 <= H < 24 and 0 <= M < 60: # 시와 분 조건
    Early_M = M - 45
    # print(H, Early_M)
    if Early_M < 0:
        H -= 1
        Early_M += 60 
        # print(H, Early_M)
        if H < 0:
            H += 24
    print(H, Early_M)