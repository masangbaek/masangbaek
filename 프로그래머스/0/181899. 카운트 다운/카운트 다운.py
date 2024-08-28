# def solution(start_num, end_num):
#     answer = []
#     # [start_num : end_num : -1]
#     for i in range(end_num, start_num + 1):
#         # print(i) 3 4 5 6 7 8 9 10
#         answer.append(i)      
#     answer.sort(reverse=True)
#     return answer

def solution(start_num, end_num):
    return list(range(start_num, end_num - 1, -1))  

    
  