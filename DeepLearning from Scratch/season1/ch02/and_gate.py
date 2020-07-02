# AND gate 구현
# coding: utf-8
import numpy as np

def AND(x1,x2):
    x = np.array([x1,x2])
    # AND 게이트 구현을 위해 정해진 파라미트 조합 중 하나(0.5,0.5,0.7)
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    # 0보다 작거나 같으면
    if tmp <= 0:
        return 0
    else:
        return 1

if __name__ == '__main__':
    for xs in [(0,0),(1,0),(0,1),(1,1)]:
        y = AND(xs[0],xs[1])
        print(str(xs) + "->" + str(y))


    



