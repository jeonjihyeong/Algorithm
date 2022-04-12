class lion:

    def __init__(self,weight,height):
        self.w=weight
        self.h=height

    def hunting(self):
        print('hunting',format(self.w*self.h))


    def sleeping(self):
        print('sleeping',format(self.h-self.w) )

    def running(self):
        print('running', format(self.w+self.h))


a=lion(60, 100)
b=lion(50, 150)
c=lion(60, 180)


a.hunting()
b.sleeping()
c.running()