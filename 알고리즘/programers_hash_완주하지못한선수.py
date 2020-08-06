


'''

객체내 count 모듈 collections.Counter(덧셈,뺄셈 가능)

'''

import collections
def solution(participant, completion):
    p = collections.Counter(participant)
    c = collections.Counter(completion)
    return list((p - c).keys())[0]



'''
hash() 함수 이용
key값이 같으면 hash값도 같은 성질을 이용

'''

def solution(participant, completion):
    
    dict={}
    temp=0
    for p in participant:
        dict[hash(p)]=p
        temp+=hash(p)
        
    for c in completion:
        temp-=hash(c)
        
        
    return dict[temp]
