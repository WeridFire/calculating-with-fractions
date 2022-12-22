class Number:

    def __init__(self, value):
        self.value = value

    def get_fraction(self):

        if(type(self.value) == 'int'):
            return self.value, 1

        

        




class Fraction:

    def __init__(self, num:Number, den:Number, npow=1, dpow=1):

        self.num:int = num
        self.den:int = den
        self.npow:int = npow
        self.dpow:int = dpow

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

    




