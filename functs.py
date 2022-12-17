from fraction import *

def find_max_divisors(a:int, b:int):

    max_div = 1

    min_num = min(a,b)
    max_num = max(a,b)

    if max_num%min_num == 0:
        return min_num

    for i in range(1,int(min_num/2)):

        if min_num%i == 0 and max_num%i==0:
            max_div = i

    return max_div

def simplify(n:Fraction):

    d:int = find_max_divisors(n.num, n.den)

    n.den = int(n.den/d)
    n.num = int(n.num/d)

    return n


fract = Fraction(898972,4)

fract.show_fraction()

fract = simplify(fract)

fract.show_fraction()

