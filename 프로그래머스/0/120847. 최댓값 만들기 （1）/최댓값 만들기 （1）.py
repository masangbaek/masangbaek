def solution(numbers):
    sorted_numbers = sorted(numbers, reverse=True)  # 리스트를 내림차순으로 정렬
    num1 = sorted_numbers[0]  # 가장 큰 값
    num2 = sorted_numbers[1]  # 그 다음 큰 값
    return num1 * num2
    