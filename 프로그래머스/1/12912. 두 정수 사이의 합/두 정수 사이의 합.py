def solution(a, b): 
    # a와 b 사이에 속한 모든 정수의 합을 구하자
    # a = 3, b = 5 -> 3 + 4 + 5 = 12
    # a == b / a or b 반환
    # a와 b는 대소 관계 정해져있지 않음
    answer = 0
    # a와 b 사이에 있는 숫자를 구하자
    if a < b:
        for i in range(a, b + 1):
            # print(i) # 3 4 5
            answer += i
    if a > b:
        for i in range(b, a + 1):
            answer += i
    if a == b:
        for i in range(a, b + 1):
            return i
            
    return answer