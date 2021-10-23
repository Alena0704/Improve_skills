    '''
    Describe problem in
    https://contest.yandex.ru/contest/28964/problems/A/
    '''
def definite_quality():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    steck = []
    c = min(len(arr1), len(arr2))
    flag=False
    if c == len(arr1):
        steck = arr2.copy()
        flag = True
    else:
        steck = arr1.copy()
    sum = 0
    if flag==False:
        for i in arr2:
            if i in steck:
                steck.remove(i)  
    print(len(arr1)-len(steck))
    else:
        for i in arr1:
            if i in steck:
                steck.remove(i) 
        print(len(arr2)-len(steck))
    '''
    Describe problem in
    https://contest.yandex.ru/contest/28964/problems/B/
    '''
def do_i_know_number():
    numbers = [int(s) for s in input().split()]
    occur_before = set()
    for num in numbers:
        if num in occur_before:
            print('YES')
        else:
            print('NO')
            occur_before.add(num)
'''
Describe problem in
https://contest.yandex.ru/contest/28964/problems/C/
'''
def unickue_elements():
    arr = list(map(int, input().split()))
    steck=[]
    bad=[]
    for i in arr:
        if i in steck and i not in bad:
            steck.remove(i)
            bad.append(i)
        elif i in bad:
            continue
        else:
            steck.append(i)
    print(" ".join(map(str,steck)))

'''
Describe problem in
https://contest.yandex.ru/contest/28964/problems/D/
'''
def game_guess_number():
    n = int(input())
    possible = set(range(1,n+1))
    s = input().strip()
    while s != "HELP":
        nums = set(map(int, s.split()))
        s = input().strip()
        if s == "YES":
            possible.intersection_update(nums)
        else:
            possible.difference_update(nums)
        s = input().strip()
    print(" ".join(map(str,possible)))

'''
Describe problem in
https://contest.yandex.ru/contest/28964/problems/E/
'''
def car_numbers():
    m = int(input())
    wits=[]
    for _ in range(m):
        wits.append(set(input().strip()))
    
    n = int(input())
    nums=[]
    maxtend=0
    for i in range(n):
        num = input().strip()
        numset=set(num)
        #nums.append([num,0])
        witend=0
        for j in wits:
            if j<=numset:
                witend +=1
        nums.append((num,witend))
        maxtend=max(maxtend, witend)
   
    ans=[]
    for num in nums:
        if num[1]==maxtend:
            ans.append(num[0])
      
    print("\n".join(ans))
         