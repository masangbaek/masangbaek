def solution(phone_number):
    result = ''
    # print(type(phone_number))
    for i in range(len(phone_number) - len(phone_number[-4:])): # 전체 길이 
        result += "*" 
    
    # 뒷 4자리 숫자 
    result += phone_number[-4:]
        # print(+phone_number[-4:])
    # print(len(phone_number) - len(phone_number[-4:]))
    return result