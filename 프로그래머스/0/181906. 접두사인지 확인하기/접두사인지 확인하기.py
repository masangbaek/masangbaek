# def solution(my_string, is_prefix):
    # 반례 : my_string에는 포함되지만 접두사가 아닌 경우
    # 예를 들어, "banana"의 모든 접두사는 "b", "ba", "ban", "bana", "banan", "banana"
#     for i in range(len(my_string)):
#         #print(my_string[i]) b a n a n a
#         if is_prefix in my_string[i]:
#             return 
#         elif is_prefix in my_string:
#             return 1
#     else:
#         return 0
def solution(my_string, is_prefix):
    if is_prefix in my_string[:len(is_prefix)]:
        return 1
    else: 
        return 0 
    
              