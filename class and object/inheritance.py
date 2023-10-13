class RSMT:
    def Course(self,course1,course2):
        self.course1=course1
        self.course2=course2

    def printd(self):
        print(self.course1,"and",self.course2)

class department(RSMT):
    def __init__(self,course1,course2):
        RSMT.__init__(self,course1,course2)


coursename="MCA"
courseduration="3 YEARs"


p1=department(coursename,courseduration)

p1.printd()
