# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# 딕셔너리?
# 영단어 숫자를 -> 숫자로 변환하는게 중요 
# def solution(s):
#     result = 0
#     # print(s) "one4seveneight" → 1478 
#     # print(type(s)) <class 'str'>
#     # dict_result = ""
#     dict = {"zero": 0,
#      "one": 1,
#      "two": 2,
#      "three": 3,
#      "four": 4,
#      "five": 5,
#      "six": 6,
#      "seven": 7,
#      "eight": 8,
#      "nine": 9
#}
    # print(s[0:3] + s[3:8] + s[8:14])
    # print(dict.keys()) dict_keys(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
    # print(dict.values()) dict_values([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    # return dict_result
    
def solution(word):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in dic:
        print(i)
        if i in word: # one, seven, eight 
            idx = str(dic.index(i)) # i의 인덱스 = 치환하려는 숫자
            word = word.replace(i, idx)
    answer = int(word)
    return answer
