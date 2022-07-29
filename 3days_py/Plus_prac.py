# Q0 Answer template

# N, X = map(int, input('N, X').split())  # N, X 를 입력받음
# data = list(map(int, input("list").split())) # 리스트를 입력받음
# answer = []
# for i in range(N):
#     if data[i]<X:
#         answer.append(data[i])
# print(answer)
#######################################################
# Q1 Answer template

# def solution(lottos, win_nums):
#     answer = []
#     g_result, b_result= [], []
#     for num in win_nums:
#         if num in lottos:
#             g_result.append(1)
#             b_result.append(1)
#     for num in lottos:
#         if num ==0:
#             g_result.append(1)
#             b_result.append(0)
#     answer.append(min(6,7-g_result.count(True)))
#     answer.append(min(6,7-b_result.count(True)))        
#     return answer

# lottos = [44, 1, 0, 0, 31, 25]
# win_nums = [31, 10, 45, 1, 6, 19]
# answer = solution(lottos, win_nums)
# print(answer)
#######################################################
# Q2 Answer template

# def solution(numbers):
#     answer = 0
#     for i in numbers:
#         answer += i
#     return 45-answer
# numbers = [1,2,3,4,6,7,8,0]
# answer = solution(numbers)
# print(answer)
#######################################################
# Q3 answer template

# def solution(store, customer):
#     answer = []
#     for i in customer:
#         s_key=len(store)//2
#         l_key=0
#         r_key=len(store)-1
#         while True:
#             if store[s_key]==i:
#                 answer.append('yes')
#                 break
#             if l_key== r_key:
#                 answer.append('no')
#                 break
#             if store[s_key]<i:
#                 l_key = s_key+1
#                 s_key = (l_key+r_key)//2
#             else:
#                 r_key = s_key-1
#                 s_key = (l_key+r_key)//2       
#     return answer

# store = [2,3,7,8,9]
# customer = [7,5,9]
# answer = solution(store, customer)
# print(answer)