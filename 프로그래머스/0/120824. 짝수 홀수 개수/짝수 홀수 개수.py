def solution(num_list):
    even = []
    odd = []
    for i in num_list:
        if i % 2 != 0:
            odd.append(i)
        else:
            even.append(i)
    return [len(even), len(odd)]
