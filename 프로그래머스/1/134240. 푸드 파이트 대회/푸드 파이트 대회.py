def solution(food):
    answer = ''
    n_food = [i if i % 2 == 0 else i - 1 for i in food ]
    # print(n_food)
    n_str = ""
    n_str1 = ''
    n_str2 = ''
    for index, i in enumerate(n_food[1:]):
        # print(index, i)
        # print(index, i)
        # print(food[3]) 음식의 수 
        n_str += str(index + 1) * (i // 2) 
        # print(n_str)
        n_str1 = "0"
        
        n_str2 = n_str[::-1]
    # print(n_str + n_str1 + n_str2)
    # print(n_str2)
    return n_str + n_str1 + n_str2
           
    # 물은 배열 중앙 위치 인덱스 0 값은 1 
    # 1번 음식 양쪽 끝
    # 인원 수 : 2먕 

