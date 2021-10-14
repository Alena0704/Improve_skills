'''
    Describe problem in:
    https://contest.yandex.ru/contest/28730/problems/B/
'''

def desicion_metro():
    n,i,j = map(int, input().split())
    dist1 = abs(j-i)-1
    dist2 = n - dist1 - 2
    print(min(dist1, dist2))

'''
    Describe problem in:
    https://contest.yandex.ru/contest/28730/problems/C/
'''

def correct(x,y,z):
  if x == y:
    return 1
  elif y<=12 and x<=12:
    return 0
  else: 
    return 1

def write_answer_to_file(answer, filename):
    with open(filename, 'w') as f_out:
        f_out.write(str(answer))

def desicion_define_wrong_date():
    stin = input()
    arr = stin.split()
    x, y, z = int(arr[0]), int(arr[1]), int(arr[2])
    assert (x>=1 and x<=31) or (y>=1 and y<=31) or (z>=1970 and z<=2069)
    write_answer_to_file(correct(int(arr[0]),int(arr[1]),int(arr[2])),'output.txt')
'''
    Describe problem in:
    https://contest.yandex.ru/contest/28730/problems/D/
''' 
def decision_school():
    N = int(input())
    arr = list(map(int, input().split()))
    print(arr[N//2])

'''
    Describe problem in:
    https://contest.yandex.ru/contest/28730/problems/E/
'''
def desicion_triangle():
    d = int(input())
    x, y = map(int, input().split())
    if x>=0 and y>=0 and x+y<=d:
        print(0)
    else:
        dist_ = [(x**2+y**2,1),((x-d)**2+y**2,2),(x**2+(y-d)**2,3)]
        print(min(dist_)[1])