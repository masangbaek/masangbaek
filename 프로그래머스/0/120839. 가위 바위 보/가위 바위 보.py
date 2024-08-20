def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    result = ''
    for i in rsp :
        result += d[i]
    return result 