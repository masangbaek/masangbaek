def solution(array):
    answer = []
    for i in array:
        if i == max(array): # 정수 배열에서 최댓값
            answer.append(i) # 최댓값을 answer 리스트에 담아준다
            index = array.index(i)
            answer.append(index)
    return answer