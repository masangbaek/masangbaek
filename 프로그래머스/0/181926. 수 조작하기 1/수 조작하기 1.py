# def solution(n, control):
#     result = n
    
#     for i in control:
#         if i == "w":
#             result += 1
#         elif i == "s":
#             result -= 1
#         elif i == "d":
#             result += 10 
#         elif i == "a":
#             result -= 10 
#     return result 
    
def solution(n, control):
    result = n
    # 0 → 1 → 0 → 10 → 0 → 1 → 0 → 10 → 0 → -1 → -2 → -1
    dicts = {
        "w" : 1,
        "s" : -1,
        "d" : 10,
        "a" : -10
    }
    for i in control:
        # print(i) w s d a w s d a s s w 
        result += dicts[i]
    return result
        