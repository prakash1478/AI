class Student:
    def __init__(self, marks1, marks2, marks3, fname, lname):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
        self.fname = fname
        self.lname = lname
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    def total(self):
        return self.marks1+self.marks2+self.marks3
    def average(self):
        return (self.marks1+self.marks2+self.marks3)/3  

student1 = Student(80, 90, 100, 'shanmuga', 'prakash')
student2 = Student(100, 80, 90, 'likhitaa', 'NJ')

print(student1.fullname())
print(student1.total())
print(student2.fullname())
print(student2.total())
print(student1.average())   
print(student2.average())