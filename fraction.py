class Number:

    def __init__(self, value, power=1):
        self.value = value
        self.power = power

    def calc_pow(self):
        res = 1
        for i in range(self.power):
            res *= self.value
        return res


class Fraction:

    def __init__(self, num:Number, den:Number):

        self.num:int = num
        self.den:int = den

    def show_fraction(self):
        if self.den != 1:
            print("{}/{}".format(self.num, self.den))
        else:
            print(self.num)

    def simplify(self):

        min_num = min(self.num,self.den)
        max_num = max(self.num,self.den)

        if max_num%min_num == 0:
            d=min_num

        else:
            for i in range(int(min_num/2),1, -1):
                if min_num%i == 0 and max_num%i==0:
                    d=min_num

        self.den = int(self.den/d)
        self.num = int(self.num/d)





