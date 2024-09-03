def solution(slice, n):
    # 피자 조각 수 slice와 피자를 먹는 사람의 수 n
    # n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판 return 
    #answer = 0
    if n % slice ==0 :
        return n // slice
    else: 
        return (n // slice) + 1
    #return answer