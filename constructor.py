class student:
    def __init__(self,x,y,z):
        self.name=x
        self.rollno=y
        self.marks=z
    def display(self):
        print("student name:{}\n rollno:{}\nmarks:{}".format(self.name,self.rollno,self.marks))
s1=student("amar",113,59)
s1.display()
s2=student("satwik",102,25)
s2.display()
s3=student("danny",152,89)
s3.display()
s4=student("sunny",202,50)
s4.display()
s5=student("susanth",162,96)
s5.display()
s6=student("pavan",182,56)
s6.display()
