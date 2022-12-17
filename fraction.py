class Number:

    def __init__(self, power=1):
        self.power = power


class Fraction:

    def __init__(self, num:Number, den:Number):

        self.num:int = num
        self.den:int = den

    def show_fraction(self):
        if self.den != 1:
            print("{}/{}".format(self.num, self.den))
        else:
            print(self.num)




