# inputs
w = 8
h = 12

# solution
import math

def solution(w, h):
    def sub_solution(a, b):
        aa, bb = [], []
        for i in range(1, a+1):
            if not a % i:
                aa.append(i)
        for i in range(1, b+1):
            if not b % i:
                bb.append(i)
        temp = set()
        for i in range(len(aa)):
            for j in range(len(bb)):
                if aa[i] == bb[j]:
                    temp.add(aa[i])
        target = max(temp)
        return target

    _w = w // math.gcd(w, h)
    _h = h // math.gcd(w, h)
    white = (_w + _h - math.gcd(_w, _h)) * math.gcd(w, h)

    black = w * h

    answer = black - white

    return answer

# run
solution(w, h)