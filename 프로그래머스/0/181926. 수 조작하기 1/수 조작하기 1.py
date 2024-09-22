def solution(n, control):
    result = n
    
    for i in control:
        if i == "w":
            result += 1
        elif i == "s":
            result -= 1
        elif i == "d":
            result += 10 
        elif i == "a":
            result -= 10 
    return result 
    
    

# def solution(n, control):
#     result = ''
#     # 0 → 1 → 0 → 10 → 0 → 1 → 0 → 10 → 0 → -1 → -2 → -1
#     dict = {
#         "w" : n + 1,
#         "s" : n - 1,
#         "d" : n + 10,
#         "a" : n - 10
#     }
#     for i in control:
#         # print(i) w s d a w s d a s s w 
#         if i in dict:
#             result += dict[i]
#     return result
        