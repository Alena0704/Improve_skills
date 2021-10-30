'''
Describe problem in
https://contest.yandex.ru/contest/29396/problems/A/

I add elements in list as separately elements - start and finish ponts.
I mark this points as 1 and -1 as start and finish segment accordingly.
Then I go to the list and have quality sum as p.
If sum p and new point's mark is positive, 
I sum difference between the coordinate of the next point and present point.
This sum is result task (res).
'''
def DecisionA():
    k = int(input())
    lst = []
    for _ in range(k):
        l, r = map(int, input().split())
        lst.append((l,1))
        lst.append((r,-1))
        
    lst.sort()
    res = 0 #result length
    p = lst[0][1] #intersecting segments
    res+=lst[1][0]-lst[0][0]
    if k>1:
        for i in range(1, k*2-1):
            if p + lst[i][1] != 0:
                res += lst[i+1][0] - lst[i][0]
            p+=lst[i][1]
    print(res)

'''
Describe problem in
https://contest.yandex.ru/contest/29396/problems/B/

I create two lists, where the first list has numbers time start,
the second list has numbers finish time.
I sort the first list in ascending order and the second list in descending order.
I memory the first value in the second list.
Then I go to the first massive and check this time is the more my memorise value (Fmin).
If it is true, I change value on the next value in the list, else I add one equipment for checking (cnt). 
cnt is result task.

The algorithm is working in O(N+log(N)), because sort is need log(N) time,
and I need O(N) time when go to the first list.
'''

def DecisionB():
    n = int(input())
    lst_x = []
    lst_y=[]
    for _ in range(n):
        T, L = map(int, input().split())
        lst_x.append(T)
        lst_y.append(T+L)
    lst_x.sort()
    lst_y.sort(reverse=True)
    cnt = 0
    F_min = lst_y.pop()
    for T in lst_x:
        if T >= F_min:
            F_min = lst_y.pop()
        else:
            cnt+=1
    print(cnt)
DecisionB()