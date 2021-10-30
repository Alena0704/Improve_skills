'''
Describe problem in
https://contest.yandex.ru/contest/29396/problems/A/
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



