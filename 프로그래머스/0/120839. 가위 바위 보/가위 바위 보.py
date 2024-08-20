def solution(rsp):
    answer = ''
    for s in rsp:
        # print(s)
        if s == '2':
            answer += '0'
            # print(s)
        elif s == '0':
            answer += '5'
        else:
            answer += '2'
    return answer