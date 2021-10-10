'''
Describe problem in
https://contest.yandex.ru/contest/28738/problems/A/
'''
def desicion_determine_max():
    maximum = 0
    num_maximal = 0
    element = -1
    while element != 0:
        element = int(input())
        if element > maximum:
            maximum, num_maximal = element, 1
        elif element == maximum:
            num_maximal += 1       
    print(num_maximal)

    '''
Describe problem in
https://contest.yandex.ru/contest/28738/problems/B/
    '''
def desicion_home_and_shops():
    arr = list(map(int, input().split()))
    shop = -20
    points = [0]*len(arr)
    for i in range(len(arr)):
        if arr[i] == 2:
            shop = i
        if arr[i] ==1:
            points[i]=i-shop
    ans = 0
    shop=30
    for i in range(len(arr)-1, -1,-1):
        if arr[i] == 2:
            shop = i
        if arr[i] ==1:
            mindist=min(shop-i,points[i])
        ans=max(ans, mindist)
        
    print(ans)

'''
Describe problem in
https://contest.yandex.ru/contest/28738/problems/C/
'''
def desicion_polindrom():
    str_ = str(input())
    max=0
    flag=False
    if len(str_)==2 and str_[0]!=str_[1]:
        print('1')
        flag=True
    for i in range(0,(len(str_)-1)//2):
        if str_[i]!=str_[len(str_)-(i)-1]:
            max+=1

    if flag==True:
        print()
    else:
        print(max)

'''
Desicion describe in
https://contest.yandex.ru/contest/28738/problems/E/
'''
def desicion_diploma_in_packages():
    n = int(input())
    lst = list(map(int, input().split()))
    print(sum(lst)-max(lst))