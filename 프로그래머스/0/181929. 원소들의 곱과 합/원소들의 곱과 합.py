def solution(num_list):
    mul = 1
    plus = 0
    for i in num_list:
        # print(i) 3 4 5 2 1
        mul *= i
        plus += i
    print(mul)
    print(plus**2)
    if mul > plus**2:
        return 0
    else: 
        return 1
        # if (sum(num_list))**2 > mul:
        #     print((sum(num_list))**2)
        #     print(mul)
        #     return 1
        # else:
        #     return 0 