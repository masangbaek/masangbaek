def solution(numbers, n):
    answer = 0
    for i in numbers:
        #print(i) 34 5 71 29 100 34
        # 앞에서 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return 
        answer += i 
        # print(answer) 34 39 110 139 239 273
        if answer > n:
            #print(answer) 139 239 273
            return answer