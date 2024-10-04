def solution(my_string):
    nums = [int(i) for i in my_string if i.isdigit()]
    # print(nums) 	[1, 2, 3, 9, 2]
    result = sorted(nums)
    return result