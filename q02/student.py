class Students:
    count = 0
    
    def __init__(self, name, age, group):
        self.name = name
        self.age = age
        self.group = group
        Students.count += 1
        
    def showDetails(self):
        print(f"""
Name: {self.name} 
Age: {self.age}
Group: {self.group}""")
        
class FirstYear(Students):
    firstYCount = 0
    
    def __init__(self, name, age, group):
        super().__init__(name, age, group)
        FirstYear.firstYCount += 1
        
class SecondYear(Students):
    secondYCount = 0
    
    def __init__(self, name, age, group):
        super().__init__(name, age, group)
        SecondYear.secondYCount += 1
        
        
pupil1 = FirstYear("Muhammad Owais", 20, "Computer Science")
pupil2 = SecondYear("Muhammad Shahaam Siddiqui", 20, "Commerce")
pupil3 = SecondYear("Muhammad Taimoor", 20, "Medical Science")


print(f"""
Total Students: {Students.count}
First Year Students: {FirstYear.firstYCount}
Second Year Students: {SecondYear.secondYCount}""")

print()


pupil1.showDetails()
pupil2.showDetails()
pupil3.showDetails()