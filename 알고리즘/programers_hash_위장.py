import collections
def solution(clothes):
    answer = 1
    st = collections.Counter([cat for _,cat in clothes])
    for i in st.values():
        # 종류별로 적어도 하나는 장착한 케이스가 됨으로 장착하지 않았을 경우도 +1 해줘야함
        answer*=(i+1)
    # 모두 장착하지 않았을 경우 -1
    return answer-1
