'''

'''
class desicion_A:
    def __init__(self):
        self.n = int(input())
        self.lst = list(map(int,input().split()))
        self.lst.sort()
        
    def func_find(self,l,r,m,t)->int:
        m = (l+r)//2
        while len(self.lst[l:r+1])>1:
            if self.lst[m]>t:
                r = m-1
            elif self.lst[m]<t:
                l=m+1
            elif self.lst[m]==t:
                break
            m = (l+r)//2
        return m
        

    def how_many_numbers(self):
        k = int(input())
        ans=[]
        for _ in range(k):
            l,r = map(int,input().split())
            l1 = self.func_find(0,self.n-1,0,l)
            r1 = self.func_find(0,self.n-1,0,r)
            #print(self.lst[l1],self.lst[r1])
            if self.lst[l1]<l or self.lst[r1]>r:
                ans.append(0)
                continue
            if l1>0:
                s = self.lst[l1-1]
                while s==self.lst[l1]:
                    l1-=1
                    if l1==0:
                        break
            if r1<self.n-1:
                s = self.lst[r1+1]
                while s==self.lst[r1]:
                    r1+=1
                    if r1==self.n-1:
                        break
            size=len(self.lst[l1:r1+1])
            ans.append(size)
        print(' '.join(map(str,ans)))

desicion = desicion_A()
desicion.how_many_numbers()