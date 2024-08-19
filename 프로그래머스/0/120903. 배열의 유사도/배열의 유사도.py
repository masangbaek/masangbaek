def solution(s1, s2):
    # 문자열 배열 s1과 s2가 주어질때 같은 원소의 개수 return 
    answer = 0
    if set(s1) & set(s2):
        # print(set(s1) & set(s2))
        answer += len(set(s1) & set(s2))
    return answer