# def solution(phone_number): 
#     # 전화번호 뒷 4자리를 제외한 나머지 숫자는 *이 되어야함 
#     result = '' # 문자열로 반환
#     back_n = ''
#     # 앞번호 *로 만들기 
#     for i in range(len(phone_number) - len(phone_number[-4:])):
#         result += "*"
#         #print(i)
#         # 번호 뒷 4자리만 남기자
#     back_n += phone_number[-4:]
        
#     return result + back_n

# def solution(phone_number): 
#     p_dict = {} # 빈 딕셔너리 만들기 
#     result = "" # 문자열 담기 
#     # 앞번호 순회할때 키와 값 정해주기 
#     for i in phone_number[:-4]:
#         p_dict[i] = "*"  
#         print(p_dict)
#         # i = 0 -> * {"0": "*"}
#         # i = 1 -> * {"1": "*"}
#     for i in p_dict.keys(): # 0, 1, 3
#         print(i)
#         result += p_dict[i] * phone_number[:-4].count(i)
        
                                                
#     return result + phone_number[-4:]

def solution(phone_number): 
    result = ""
    result += phone_number.replace(phone_number[:-4], "*" * len(phone_number[:-4]))
    return result
    