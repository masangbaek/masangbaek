def solution(food): # food 의 인덱스 : 음식종류, 원소 : 음식갯수
    result = '' # 결과가 문자열이다.
    # 1. "122333" 구현하기
    # 한사람 먹을 분량으로 나눠주자
    n_food = [i // 2 for i in food]
    result1 = ''
        
    for index, i in enumerate(n_food[1:]): # 인덱스 0은 물이니까 필요없음
        # print(index, i) # 0 1 / 1 3 / 2 4 / 3 6 -> 0 3 / 1 4 / 2 6
        # enumerate는 인덱스 0부터 시작한다.
        # 1 3 / 2 4 / 2 6 을 구현해야한다
        
        # 문자열로 바꾸자 / 인덱스 + 1 을 해서 1부터 나오게 하자
        result += str(index + 1) * i
        # print(result) 
        
        # 2. 0 더해서 연결하기
        
        # 3. 1번 뒤집기

    result1 += result[::-1]
        
    
    return result + "0" + result1