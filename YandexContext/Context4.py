'''
Describe problem in
https://contest.yandex.ru/contest/28970/problems/A/
'''
def Aligator_express():
    n = int(input())
    d={}

    for _ in range(1,n+1):
        di, ki = map(int, input().split())
        if d.get(di) != None:
            d[di] = ki + d[di]
        else:
            d[di] = ki
    d = sorted(d.items(), key=lambda x: x[0])
    for k,v in d:
        print(k,v)

'''
Describe problem in
https://contest.yandex.ru/contest/28970/problems/B/
'''
def electons_in_USA():
    d = {}
    fin = open('input.txt', 'r', encoding='utf8')
    for line in fin:
        cand, choice = line.split()
        
        if d.get(cand) != None:
            d[cand] += int(choice)
        else:
            d[cand] = int(choice)
    fin.close()
    d = sorted(d.items(), key=lambda x: x[0])
    for k,_ in d:
        print(k, _)
    fin.close()

    '''
    Describe problem in
https://contest.yandex.ru/contest/28970/problems/C/
    '''
def frequency_analysis():
    d = {}
    fin = open('input.txt', 'r', encoding='utf8')
    for line in fin:
        words = line.split()
        for i in words:
            if d.get(i) != None:
                d[i] += 1
            else:
                d[i] = 1
    fin.close()
    d = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    for k,_ in d:
        print(k)

'''
Describe problem in
https://contest.yandex.ru/contest/28970/problems/D/
'''

def elections_in_Duma():
    parties = {}
    sum =0
    with open('input.txt', 'r', encoding='utf8') as fin:
        for num, line in enumerate(fin):
            lst=[]
            words = line.split()
            cnt = int(words[-1])
            partiname = ' '.join(words[:-1])
            parties[partiname] = lst
            parties[partiname].append(num)
            parties[partiname].append(cnt)
            sum += cnt

    f = sum/450
    free = 450
    for k,v in parties.items():
        v.append(v[1]//f)
        v.append(v[1]%f)
        free -= v[1]//f
    d = sorted(parties.items(), key=lambda x: x[1][3], reverse=True)

    for i in range(int(free)):
        d[i][1][2]+=1
    d = sorted(d, key=lambda x: x[1][0])
    for i in d:
        print(i[0], int(i[1][2]))
'''
Describe problem in
https://contest.yandex.ru/contest/28970/problems/E/

'''

def Forum():
    n = int(input())
    reply = [0]*n
    topics = ['']*n
    for i in range(n):
        num = int(input())
        if num == 0:
            reply[i] = i
            topics[i] = input()
            input()
        else:
            reply[i] = reply[num-1]
            input()
    cntreplies = {}
    for i in reply:
        cntreplies[i] = cntreplies.get(i,0)+1
    ans=[]
    for t in cntreplies:
        ans.append((-cntreplies[t], t)) 

print(topics[min(ans)[1]])