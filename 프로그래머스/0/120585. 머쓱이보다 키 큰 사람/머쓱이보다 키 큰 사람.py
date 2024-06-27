def solution(array, height):
    answer = 0
    for i in array: # [149, 180, 192, 170]
        if i > height:
            answer += 1 # 머쓱이보다 키가 큰 사람이 있을때마다 더해주자
    return answer