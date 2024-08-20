#     # 소문자라면 대문자로 변환
#     # 대문자라면 소문자로 변환
# def solution(my_string):
#     answer = my_string.swapcase()
#     return answer

def solution(my_string):
    answer = ''
    for s in my_string:
        if 'a'<=s<='z':
            answer += s.upper()
        else:
            answer += s.lower()
    return answer
