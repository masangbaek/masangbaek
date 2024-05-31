def solution(my_string):
    table = my_string.maketrans("","","aeiou")
    return my_string.translate(table)
  