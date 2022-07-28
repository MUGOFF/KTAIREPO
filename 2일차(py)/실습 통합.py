# -*- coding: utf-8 -*-
# def f():
    # name = input('이름')
    # print(f'Hello {name}');
    #############################################

    # a = int(input('정수 a값'))
    # b = int(input('정수 b값'))
    # c = int(input('정수 c값'))
    # d = int(input('정수 d값'))
    
    # med =0
    # maxi = a
    # if b>maxi:
    #     maxi=b;
    # if c>maxi:
    #     maxi=c;
    # if d>maxi:
    #     maxi=d;

    # print(f'최대값은 {maxi}다')
    ########################################
    # if a>= b:
    #     if b>=c:
    #         med= b;
    #     elif a<=c:
    #         med = a;
    #     else:
    #         med =c;
    # elif a>c:
    #     med =a;
    # elif b>c:
    #     med =c;
    # else:
    #     med =b;
    # print(f'중앙값은 {med}다')
    #############################################
    # wateruse = int(input('수도사용량(liter)'))
    # com=input('회사')
    # waterpay=0
    # if com =='a':
    #     waterpay=wateruse*100
    # else:
    #     if wateruse<=50:
    #         waterpay= wateruse*150
    #     else:
    #         waterpay=150*50+(wateruse-50)*75
    # print(f'수도요금은 {waterpay}')
    ##############################################
    # print('a부터 b까지 정수의 합을 구합니다.')
    # a = int(input('정수 a를 입력하세요.: '))
    # b = int(input('정수 b를 입력하세요.: '))
    # if a > b:
    #     a, b = b, a
    # sum = 0
    # for i in range(a, b):
    #     print(f'{i} + ', end='')
    #     sum +=i
    # sum +=b
    # print(f'{b} = {sum}')
    ############################################
    # sq = int(input('직사각형의 넓이를 입력하세요 :'))
    # for i in range(1,sq+1):
    #     if sq%i: continue;
    #     print(f'{i} X {sq//i}')
    ###############################################    
# f();
#############################
# def elecP(usage):
#     charge = 0
#     re_charge = 0
#     if usage <100:
#         charge += 410        
#         charge += usage*60.7        
#     elif usage <= 200:
#         charge += 910        
#         charge += 60.7*100 + (usage-100)*125.9        
#     else:
#         charge +=1600        
#         charge += 60.7*100 + 125.9*100 + (usage-200)*187.9
    
#     re_charge += charge +charge*0.1
#     re_charge += charge*0.037
#     print(f'전력 요금은 : {int(charge)}원 \n 총 전기 요금 : {int(re_charge)}원')

# ele = int(input('전기 사용량: '))
# elecP(ele);  
######################################################
# plma = int(input('횟수'))
# print('+-'*(plma//2),end='')
# if plma%2:
#     print('+')
# print()
#######################################################
# a=int(input('수'))
# for i in range(1,a+1):
#     if i==8:
#         continue
#     print(f'{i} ',end='')
# print()
###############################################################
# a=int(input('수'))
# b=0
# for i in range(1,a+1):
#     for j in range(2,6):
#         if i**j == a:
#             print(f'{i}의 {j}제곱')
#             b=1

# if b==0:
#     print('없음')
#################################################################

# # Q0 Answer template
# def gcd_sol(a, b):
    #   if a==b:
    #       answer=a
    #       return answer
#     answer = -1
#     for i in range(1,a+1):
#         if a%i or b%i:
#             continue
#         answer = i
#         if i>=b:
#             break
#     return answer
# # Q1 Answer template
# def lcm_sol(a, b):
#     answer = a
    #   if a==b:
    #       return answer
#     while True:
#         if not(answer%a or answer%b):
#             break
#         answer +=1
#     return answer


# n1 = int(input('수1 : '))
# n2 = int(input('수2 : '))
# c= gcd_sol(n1,n2)
# print(f'GCD : {c}')
# n1 = int(input('수1 : '))
# n2 = int(input('수2 : '))
# c= lcm_sol(n1,n2)
# print(f'LCM : {c}')

# Q2 Answer template
# 내 풀이
# N = int(input('수 입력: '))
# NN=N
# count = 0
# while True:
#     if N<10:
#         N = N*11
#     else:
#         temp= N//10+N%10
#         N= temp%10+((N%10)*10)
#     count+=1
#     if NN == N:
#         break
# print(count)

# Q3 Answer template
# def plma_sol(left, right):
#     if left>right:
#         left, right = right, left
#     answer = 0
#     # for i in range(left, right+1):
#     #     count =0
#     #     for j in range(1,i+1):
#     #         if i%j:
#     #             continue
#     #         count +=1
#     #     if count%2:
#     #         answer -=i
#     #     else:
#     #         answer +=i     
#     # return answer
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
# Q4 Answer Template
# data = input('숫자로 이루어진 문자열을 입력하세요. ')
# result = 0
# print('0',end='')
# for i in range(len(data)):
#     n = int(data[i])
#     if result*n >= result+n:
#         result *=n
#         print(f'x{n}',end='')
#     else:
#         result +=n
#         print(f'+{n}',end='')
# print('=',result)
# Q5 Answer Template
# n = input('숫자를 입력하세요. ')
# left =0
# right =0
# if len(n)%2:
#     print('Ready')
# else:
#     for i in range(len(n)):
#         if i < len(n)//2:
#             left += int(n[i])
#         else:
#             right += int(n[i])
#     if left == right:
#         print("LUCKY")
#     else:
#         print('ready')
# Q6 Answer template

# def sq_sol(n):
#     answer = 0
#     while True:
#         if answer*answer == n:
#            answer +=1
#            return answer*answer
#         if answer*answer > n:
#             return -1
#         answer+=1
# n1 = int(input('수 : '))
# c = sq_sol(n1)
# print(c)
