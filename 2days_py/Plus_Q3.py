# Q3 Answer template
# def plma_sol(left, right):
#     if left>right:
#         left, right = right, left
#     answer = 0
#     for i in range(left, right+1):
#         for j in range(1,i+1):
#             if j*j == i:
#                 answer -= i
#                 break
#             if j==i:
#                 answer += i
#     return answer

# n1 = int(input('수1 : '))
# n2 = int(input('수2 : '))
# c = plma_sol(n1,n2)
# print(c)