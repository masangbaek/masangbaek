def solution(n):
    answer = []
    for i in reversed(str(n)):
        print(i)
        answer.append(int(i))
    return answer

