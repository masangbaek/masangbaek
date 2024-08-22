def solution(arr):
    answer = []
        
    
    for i in arr:
        #print(i) 1 2 3 100 99 98
        # 1. arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수 2로 나누고
        if (i >= 50) & (i % 2 == 0):  
            answer.append(i / 2) 
            #print(i) 100 98 -> 50 49
        # 2. 50보다 작은 홀수라면 2를 곱함
        elif (i < 50) & (i % 2 != 0):
            answer.append(i * 2)
            #print(i) 1 3 -> 2 6
        # 3. 1,2번에 해당하지 않다면 그냥 반환
        else:
            answer.append(i)
        # 4. 결과를 정수 배열로 return 
    
    return answer