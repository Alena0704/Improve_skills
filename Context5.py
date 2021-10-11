'''
Describe problem in
https://contest.yandex.ru/contest/29075/problems/A/
'''
def prefix_sum():
    with open('input.txt') as f:
        n, q = map(int, f.readline().split())
        numbers = list(map(int, f.readline().split()))
        prefix_sums = [0]
        for i in range(n):
            prefix_sums.append(prefix_sums[i] + numbers[i])
        for i in range(q):
            l, r = map(int, f.readline().split())
            print(prefix_sums[r] - prefix_sums[l-1])

class decision:
    def __init__(self):
        self.n, self.r = map(int, input().split())
        self.lst = list(map(int, input().split()))
        self.arr = [0 for j in range(self.n*2)]
        for k in range(self.n*2-1, self.n-1, -1):
            self.arr[k]=self.lst[k-self.n]
        for k in range(self.n-1, 0, -1):
            self.arr[k] = self.arr[k*2]+self.arr[k*2+1]

    def get_lens(self):
        for i in range(self.r):
            print(self.get_sum())

    def get_sum(self):
        left, right = map(int, input().split())
        sum_=0
        l=self.n+left-1
        r=self.n+right-1    
        while True:
            if l%2==1:
                sum_+=self.arr[l]
            if r%2==0:
                sum_+=self.arr[r]
            if l%2==0:
                l=l//2
            else:
                l=l//2+1
            if r%2==1:
                r=r//2
            else:
                r=r//2-1
            if l>r:
                break
            if l==r:
                sum_+=self.arr[l]
                break
        return sum_

des = decision()
des.get_lens()

'''
Describe problem in
https://contest.yandex.ru/contest/29075/problems/B/
'''
def max_sum():
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_sub_array(arr))

def max_sub_array(A):
    curr_max_sum = float('-inf')
    global_max = float('-inf')
    for i in A:
        curr_max_sum = max(curr_max_sum + i, i)
        global_max = max(curr_max_sum, global_max)
    return global_max
def max_sum_subseq(items):
    iter_items = iter(items)
    try:
        temp_sum = next(iter_items)
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_items:
        temp_sum = max(temp_sum + item, item)
        max_sum = max(temp_sum, max_sum)
    return max(max_sum, 0)

def max_sum2():
    n = int(input())
    arr = list(map(int, input().split()))
    print(max_sum_subseq(arr))
def max_sum_subseq(items):
    iter_items = iter(items)
    try:
        temp_sum = next(iter_items)
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_items:
        temp_sum = max(temp_sum + item, item)
        max_sum = max(temp_sum, max_sum)
    return max(max_sum, 0)
'''
Describe problem in
https://contest.yandex.ru/contest/29075/problems/C/
'''
def eberubody_have_computer():
    n,m = map(int, input().split())
    x = readannum()
    y = readannum()
    ynum=0
    ans=[0]*(n+1)
    cnt=0
    for peop, xnum in x:
        while ynum<len(y) and y[ynum][0]<peop+1:
            ynum+=1
        if ynum==len(y):
            break
    ans[xnum]=y[ynum][1]
    ynum+=1
    cnt+=1
    #print("{}\n".join(map(str, ans[1:])))
    print(cnt)
    print(*ans[1:])
def readannum():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        x[i] = (x[i], i+1)
    x.sort()
    return x
'''
Describe problem in
https://contest.yandex.ru/contest/29075/problems/D/
'''
def right_bracket_construction():
    lst = input()
    check=[]
    flag=False
    for i in lst:
        if i=='(':
            check.append(i)
        else:
            try:
                check.pop()
            except:
                print('NO')
                flag=True
                break
    if len(check)==0 and flag==False:
        print('YES')
    elif len(check)>0 and flag==False:
        print('NO') 
'''
Describe problem in
https://contest.yandex.ru/contest/29075/problems/E/
'''
def sum_tree_numbers():
    s=int(input())
    a = readannum()
    b = readannum()
    c = readannum()
    c.sort(key = lambda x: (x[0], -x[1]))
    flag=False
    for aval, apos in a:
        cpos =len(c)-1
        for bval, bpos in b:
            while cpos>0 and aval + bval + c[cpos][0]>s:
                cpos-=1
            if aval + bval + c[cpos][0]==s and (not flag or (apos,bpos,cpos)<ans):
                ans=apos,bpos,c[cpos][1]
                flag=True
    if flag:
        print(*ans)
    else:
        print(-1)

def readannum():
    x = list(map(int, input().split()))[1:]
    for i in range(len(x)):
        x[i] = x[i], i
    x.sort()
    return x