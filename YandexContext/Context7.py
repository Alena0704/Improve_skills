'''
Describe problem in
https://contest.yandex.ru/contest/29396/problems/A/
'''
def DecisionA():
        k = int(input())
        dict_ = {}
        for _ in range(k):
            L,R = map(int, input().split())
            if L==R:
                continue
            if len(dict_)==0:
                dict_[(L,R)] = R-L
                continue
            del_s, del_e = -1, -1
            for elem in dict_:
                s, e = elem[0], elem[1]
                if L >=s and L < e:
                    if R > e:
                        dict_[(s,R)] = R-s
                        del_s = s
                        del_e = e
                        break
                    else:
                        continue
                elif R >= s and R < e:
                    if L < s:
                        dict_[(L,e)] = e-L
                        del_s = s
                        del_e = e
                        break
                    else:
                        continue
                dict_[(L,R)] = R-L
            if del_s * del_e > 0:
                del dict_[(del_s, del_e)]
        
        length = sum(dict_.values())
        return length

k = int(input())
dict_={}
for i in range(k):
	h_s, h_f, g = map(int, input().split())
	if (h_s, h_f) not in dict_:
    		dict_[(h_s, h_f)] = g+1
	else:
		    dict_[(h_s, h_f)] += g+1
keys = list(dict_.values())
keys.sort()
print(keys[0])
