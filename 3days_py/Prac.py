#Q1
# a=[2]
# for i in range(2,1000):
#     for j in range(2,i):
#         if not(i%j):
#             break
#         if j==i-1:
#             a.append(i)
# print(a)
################################################
#Q2
# a=[]
# while True:
#     x=input('리스트 원소 입력: ')
#     if x=='end' or x== '':
#         break
#     a.append(x)
# print(a)
# for i in range(len(a)//2):
#     a[i], a[-i-1] = a[-i-1], a[i]
# print(a)
################################################
#Q3
# def search_key(li,key):
#     index=0
#     for i in a:
#         if i==key:
#             return index
#         index +=1
#     return 0
# a=[]
# while True:
#     x=input('리스트 원소 입력: ')
#     if x=='end' or x== '':
#         break
#     a.append(x)
# n=input("찾을 값: ")
# if search_key(a,n):
#     print(f'위치는 a[{search_key(a,n) }]')
# else:
#     print('없음')
################################################
#Q4
# def maxof(a):
#     maxi=0
#     co=0
#     maxx=a[0]
#     for i in a:
#         if i>maxx:
#             maxx=i
#             maxi=co
#         co +=1
#     return maxx, maxi
# a=[]
# while True:
#     x=input('리스트 원소 입력: ')
#     if x=='end' or x== '':
#         break
#     a.append(x)
# print(f'최대값{maxof(a)[0]}, 최대값인덱스{maxof(a)[1]}')
