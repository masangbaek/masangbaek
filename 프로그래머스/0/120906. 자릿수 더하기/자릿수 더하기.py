def solution(n):
    answer = []
    answer += str(n)
    # print(answer) ["1","2","3","4"]
    return sum(list(map(int, answer)))