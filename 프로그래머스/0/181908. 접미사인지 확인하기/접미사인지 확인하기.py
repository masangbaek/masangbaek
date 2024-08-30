def solution(my_string, is_suffix):
    if is_suffix in my_string[-len(is_suffix):]:
        return 1 
    else: 
        return 0
    #return my_string[1:len(is_suffix)+1]
 
