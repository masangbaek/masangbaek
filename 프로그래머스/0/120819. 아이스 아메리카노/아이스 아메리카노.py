# def solution(money):
#     # print(money)  
#     # 5500 = 5500 * 1 + 0
#     # 15000 = 5500 * 2 + 4000
#     result = [] # [max커피, 잔돈]
#     money = 5500 * (x + 1) + money
#     #return result

# def solution(money):
#     a = money // 5500
#     b = money % 5500
 
#     return [a, b]

def solution(money):
    result = []
    n = money // 5500 
    result.append(n)
    result.append(money-(n * 5500))
    return result