def solution(num_list):
    # 리스트의 길이가 11이상이면 합
    if len(num_list) >= 11:
        #print(len(num_list))
            answer = sum(num_list)
    # 리스트의 길이가 10이하이면 곱        
    else:
        #print(len(num_list))
            answer = 1
            for element in num_list:
                #print(element)
                answer *= element
            
    return answer
        


