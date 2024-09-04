def solution(num_list):
    answer = []
    for i in num_list:
        #print(i) 2 1 6 
        if num_list[-1] > num_list[-2]:
            answer += num_list
            answer.append(num_list[-1] - num_list[-2])
            return answer
    
        else: 
            answer += num_list
            answer.append(num_list[-1] * 2)
            return answer