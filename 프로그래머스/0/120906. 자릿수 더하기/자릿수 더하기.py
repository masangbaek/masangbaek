# def solution(n):
#     answer = []
#     answer += str(n)
#     # print(answer) ["1","2","3","4"]
#     return sum(list(map(int, answer)))

def solution(n):
    n = str(n)
    answer = 0 
    for i in n:
        # print(i) 1 2 3 4
        answer += int(i)
    return answer