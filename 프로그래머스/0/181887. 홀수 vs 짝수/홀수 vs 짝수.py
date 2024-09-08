def solution(num_list):
    for i in num_list:
        # print(i) 4 2 6 1 7 6
        # 짝수 번째와 홀수번째 비교
        # print(num_list[1::2]) 짝수 2 1 6
        # print(num_list[::2]) 홀수 4 6 7
        if sum(num_list[1::2]) > sum(num_list[::2]):
            return sum(num_list[1::2])
        # # 두 값이 같을 경우
        else:   
            return sum(num_list[::2]) or sum(num_list[1::2])