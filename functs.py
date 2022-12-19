from fraction import *

def find_max_divisor(a:int, b:int):

    min_num = min(a,b)
    max_num = max(a,b)

    if max_num%min_num == 0:
        return min_num

    for i in range(int(min_num/2),1, -1):

        if min_num%i == 0 and max_num%i==0:
            return i

def simplify(n:Fraction):

    d:int = find_max_divisor(n.num, n.den)

    n.den = int(n.den/d)
    n.num = int(n.num/d)

    return n


fract = Fraction(121, 11)

fract.show_fraction()

fract = simplify(fract)

fract.show_fraction()

