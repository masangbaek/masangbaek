def solution(num_list, n):
    # answer = [ + 1 for i in range(n) for j in range(n)]
    # return answer
    
    # 2차원 배열로 바꿀 때 들어갈 원소의 수 
    result = []
    for i in range(len(num_list) // n): # 2일 경우 0부터 1까지 반복 
        # print(i) # 0 1 2 3
        new = []
        for j in num_list:
            # print(j) 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8
            new.append(j) # [1,2,3,4,5,6,7,8]
            new = num_list[i * n : (i + 1) * n]
        result.append(new) 
    return result # [[1,2,3,4,5,6,7,8]]
      

  
            