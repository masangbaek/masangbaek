def solution(phone_number): 
    # 전화번호 뒷 4자리를 제외한 나머지 숫자는 *이 되어야함 
    result = '' # 문자열로 반환
    back_n = ''
    # 앞번호 *로 만들기 
    for i in range(len(phone_number) - len(phone_number[-4:])):
        result += "*"
        # 번호 뒷 4자리만 남기자
    back_n += phone_number[-4:]
        
    return result + back_n