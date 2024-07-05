a, b = map(int, input().strip().split(' '))
# print(a + b)

# result = ''
# for i in range(1, b + 1):
#     result += "\n"
#     for j in range(1, a + 1):
#         result += "*"
# print(result)

for i in range(b):
    for j in range(a):
        print("*", end="")
    print()