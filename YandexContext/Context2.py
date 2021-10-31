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

    Class DecisionB get list buildings: 1 - living home, 2 - shop, 3 - office.
    We have to find maximum distance for nearest shop from living house.
    In prerocess I perfom points as minimal distance from living house to shop.
    If I find shop, I remember coordinate. 
    If I find living house, I remember for this coordinate difference between remember shop and this coordinate.
    When I get answer, I also go ro list in reduse order, but logic work is the same.
    If I find shop, I remember coordinate.
    If I find living house, I consider between safe values in list 
    and choose minimum value between remember value and new difference between remember shop and this coordinate. 
    Then I check is this value is more them maximum distance.

    The computational complexity is O(N^2), because we have to go to the list two times.
    '''

class DecisionB:

    def __init__(self):
        self.arr = list(map(int, input().split()))
        self.n = len(self.arr)
        self.points=[]

    def __preprocess(self):
        shop=-20
        self.points = [0]*self.n
        for i in range(self.n):
            if self.arr[i] == 2:
                shop = i
            if self.arr[i] ==1:
                self.points[i]=i-shop

    def get_answer(self):
        ans = 0
        shop=30
        for i in range(self.n-1, -1,-1):
            if self.arr[i] == 2:
                shop = i
            if self.arr[i] ==1:
                mindist=min(shop-i,self.points[i])
            ans=max(ans, mindist)
        print(ans)

    '''
    Describe problem in
    https://contest.yandex.ru/contest/28738/problems/C/

    I go to list of simbols of half of word.
    I check current simbol is the same the mirror final simbol.
    If it is not, I add one.
    Mirror simbol is length of word minus k. k is current iterator simbol in the word.
    '''

def desicion_polindrom():
    str_ = str(input())
    max=0
    flag=False
    if len(str_)==1:
        print('0')
        flag=True
    elif len(str_)==2 and str_[0]!=str_[1]:
        print('1')
        flag=True
    for i in range(0,(len(str_))//2):
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