def solution(numbers):
    numbers.sort()
    # print(numbers)
    return numbers[-1] * numbers[-2]
    