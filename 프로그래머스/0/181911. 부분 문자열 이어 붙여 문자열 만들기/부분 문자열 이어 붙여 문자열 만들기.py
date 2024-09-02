def solution(my_strings, parts):
    result = ''
    # print(parts) 	[[0, 4], [1, 2], [3, 5], [7, 7]]
    # for i in range(len(my_strings)):
        # print(i) 0 1 2 3
        # print(parts[i]) [0, 4]
        # return my_strings[i]  # progressive
        # result = [my_strings[start:end] for start, end in parts]
        # return result
    for i, (start, end) in enumerate(parts):
        # print(start, end) 0 4 1 2 3 5 7 7
        # print(my_strings[start : end])
        # print(i, (start, end)) 0 (0, 4)
        if i < len(my_strings):
            substring = my_strings[i][start:end + 1]  # 각 문자열에 대해 슬라이싱
            result += substring
        else:
            result += ''  # 범위를 벗어나면 빈 문자열 추가
    return result
