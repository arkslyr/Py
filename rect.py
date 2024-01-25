class Rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        self.area=self.l*self.b
    def __lt__(self,a):
        if self.area<a.area:
            print(self.area,"is less than ",a.area)
        else:
            print(a.area,"is less than ",self.area)

r1=Rect(3,4)
r2=Rect(3,6)
print(r1<r2)
