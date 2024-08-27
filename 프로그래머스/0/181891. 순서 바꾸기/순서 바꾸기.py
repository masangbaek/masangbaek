def solution(num_list, n):
    answer1 = []
    answer2 = []
    for idx, num in enumerate(num_list):
        # print(idx, num) 
        if idx >= n: # 인덱스 자리가 n
            answer1.append(num)
        else: 
            answer2.append(num)
    return answer1 + answer2