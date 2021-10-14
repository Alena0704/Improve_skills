'''
Describe problem in
https://contest.yandex.ru/contest/29188/problems/A/
https://contest.yandex.ru/contest/29188/problems/B/
'''
from typing import List
class decision_A_B(object):        
    def __init__(self, lst: List[int], n:int):
        self.n = n
        self.lst = lst
        self._preprocess()

    def _preprocess(self):
        pass
class desicion_A(decision_A_B):
    def __init__(self):
        n = int(input())
        lst = list(map(int,input().split()))
        super().__init__(lst, n)
        self._preprocess()
        
    def __init__(self, lst: List[int], n: int):
        super().__init__(lst, n)
        self._preprocess()

    def _preprocess(self):
        self.lst.sort()
        
    def func_find(self,t: int)->int:
        l = -1
        r = self.n
        m = (l+r)//2
        while l+1<r:
            m = (l+r)//2
            if self.lst[m]<=t:
                l=m
            else:
                r=m
        return l
        
    def get_numbers_in_l_r(self, l: int,r: int) -> int:
        cnt = self.func_find(r)-self.func_find(l-1)
        return cnt

    def how_many_numbers(self):
        k = int(input())
        ans=[]
        for _ in range(k):
            l,r = map(int,input().split())
            ans.append(self.get_numbers_in_l_r(l,r))
        print(' '.join(map(str,ans)))

#desicion = desicion_A()
#desicion.how_many_numbers()

class decision_B(decision_A_B):
    def __init__(self):
        n = int(input())
        lst = list(map(int,input().split()))
        super().__init__(lst,n)
        self.lst.append(-1)
        self.dict_={}
        self._preprocess()
    def __init__(self, lst: List[int], n: int):
        super().__init__(lst, n)
        self.dict_={}
        self.lst.append(-1)
        self._preprocess()
        
    def _preprocess(self):
        self.lst.append(-1) #This is necessary in B
        self.dict_={}
        ch = self.lst[0]
        index=0
        for ind,i in enumerate(self.lst):
             if i!=ch:
                 self.dict_[ch] = (index,ind-1)
                 index = ind
                 ch = i
    def determine_borders(self,m):
        if m in self.dict_:
                a,b = self.dict_[m]
                return (a+1,b+1)
        else:
                return (0,0)

    def left_right_border2(self):
        k = int(input())
        ans=[]
        arr = list(map(int,input().split()))
        for index in range(k):
            m = arr[index]
            ans.append(self.determine_borders(m))
        for i,j in ans:
            print('{} {}'.format(i,j))

    
'''
Describe problem:
https://contest.yandex.ru/contest/29188/problems/C/
'''
def get_squere_expression(a,b,c):
    if a*b*c==0:
        D = b**2-4*a*c
        if D>0:
            return ((-b+D**0.5)//(2*a),(-b-D**0.5)//(2*a))
        elif D==0:
            return (-b//(2*a))
        else:
            None
    else:
        if a==0:
            return get_cube_with_b(b,c)
        if b==0:
            return get_cube_with_c(a,c)

def get_cube_with_b(a,b):
    if a!=0:
        return -b/a
    elif a==0:
        return None
    else:
        return 0

def get_cube_with_c(a,b):
    if b<0:
        if a!=0:
            return ((-b/a)**0.5, -(-b/a)**0.5)
        else:
            return 0
    elif b==0:
        return 0
    else:
        return None

def get_desicion_square(a,b,c,d):
    answer=[]
    if a == 0:
        ans = get_squere_expression(b,c,d)
        if ans != None:
            answer.append(ans)
    elif d ==0:
        ans = get_squere_expression(a,b,c)
        if ans != None:
            answer.append(ans)
    elif b==0:
        ans = get_cube_with_c(a,b)
        if ans != None:
            answer.append(ans)
            answer.append(0)
    elif c==0:
        ans = get_cube_with_b(a,c)
        if ans != None:
            answer.append(ans)
            answer.append(0)

def get_numbers(number):
    lst = []
    for i in range(number):
        if number%i==0:
            lst.append(i)
            lst.append(-i)
def get_decision_cube(a,b,c,d):
    answer = []
    if a+b+c+d==0:
        return 1
    elif b+d==a+c:
        return -1
    else:
        candidats = get_numbers(a) + get_numbers(d)
        for i in candidats:
            if a*i**3+b*i**2+c*i+d==0:
                answer.append(i)

def get_definite_null(a,b,c,d):
    if a*b*c*d==0:
        get_desicion_square(a,b,c,d)
    else:
        get_decision_cube(a,b,c,d)

def get_decision_exercise():
    a,b,c,d = map(int, input().split())
    if a*b*c*d==0:
        get_definite_null(a,b,c,d)
class expression:
    def __init__(self):
        self.a,self.b,self.c,self.d = map(int, input().split())
        self.__preprocess()
    def __init__(self, a,b,c,d):
            self.a,self.b,self.c,self.d = a,b,c,d
            self.__preprocess()
    def __preprocess(self):
        if self.a<0:
            self.a = -self.a
            self.b = -self.b
            self.c = -self.c
            self.d = -self.d
    
    def f(self,x):
        return self.a*x**3+self.b*x**2+self.c*x+self.d
    def root(self,eps = 0.0000001):
        left = -2000
        right = 2000
        while right-left>eps:
            m = (right+left)/2
            if self.f(m)>0:
                right=m
            else:
                left=m
        return (left+right)/2
            


'''
Describe problem:
https://contest.yandex.ru/contest/29188/problems/D/
'''

'''
Describe problem:
https://contest.yandex.ru/contest/29188/problems/E/
'''
