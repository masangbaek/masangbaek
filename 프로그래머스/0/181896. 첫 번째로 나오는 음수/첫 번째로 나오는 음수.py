def solution(num_list) :
    answer = 0
    for i in range(len(num_list)):
        #print(i)
        if num_list[i] < 0:
            #print(i) -2
            return i
    else:
        return -1
