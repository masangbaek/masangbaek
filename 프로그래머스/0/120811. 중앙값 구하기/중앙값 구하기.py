def solution(array):
    array.sort()  # array를 sort()로 오름차순 정렬을 해줍니다.
    # print(array)
    mid_num = len(array) // 2
    # 중앙값을 결과로 반환합니다.
    return array[mid_num]