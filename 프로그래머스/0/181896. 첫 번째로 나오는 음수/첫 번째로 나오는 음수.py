# 1
# def solution(num_list) :
#     answer = 0
#     for i in range(len(num_list)):
#         #print(i)
#         if num_list[i] < 0:
#             #print(i) -2
#             return i
#     else:
#         return -1

def solution(num_list):
    for idx, num in enumerate(num_list):
        #print(i, num) 0 12 / 1 4 / 2 15 ...
        if num < 0:
            return idx
        
    return -1