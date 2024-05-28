def solution(n):
    answer = []
     #range(start, stop, step)
        #range(0, 100, 2) [0, 2, 4, ]
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer