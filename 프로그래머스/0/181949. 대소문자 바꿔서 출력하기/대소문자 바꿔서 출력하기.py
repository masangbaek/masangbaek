str = input()

result = ""
for i in str:
    # print(i)
    if i.islower():
       result += i.upper()
    else:
        result += i.lower()
        
print(result)