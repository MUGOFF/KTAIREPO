#MINIQ1
# def min_of(li):
#     ans = li[0]
#     for i in li:
#         if i <ans:
#             ans = i
#     return ans
# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']
# print(min_of(t))
# print(min_of(s))
# print(min_of(a))
#MINIQ2
# def rev_pri(li):
#     print('리스트 역순 출력')
#     for i in range(len(li)-1,-1,-1):
#         print(li[i])
# num = int(input('원소 수를 입력하세요.: '))
# x = [None] * num # 원소 수가 num인 리스트를 생성
# for i in range(num):
#     x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
# rev_pri(x)
#MINIQ3
def search_count(a,key):
    lin_count = 0
    sen_count = 0
    lin_i=0
    sen_i=0
    while True:
        if lin_i==len(a):
            lin_i=-1
            break
        if a[lin_i]==key:
            break
        lin_i+=1
        lin_count+=1
        
    b=a.copy()
    b.append(key)
    while True:
        if b[sen_i]==key:
            break
        sen_i+=1
        sen_count+=1
    if sen_i == len(b)-1:
        sen_i = -1     
    return lin_count, sen_count,lin_i,sen_i

a=[2, 5, 1, 3, 9, 6, 7]
n=int(input('검색값: '))
print(search_count(a,n))