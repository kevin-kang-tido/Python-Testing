
## TODO: review function 

class students: 
    def __init__(self, name, gender, score, grade):
        self.name = name
        self.gender = gender
        self.score = score
        self.grade = grade
    def intro(self):
        return f'Student Name: {self.name}, Gender: {self.gender}, Score: {self.score}, Grade: {self.grade}'
    


## TODO: create the obj for the student 
student1  = students("Kevin","Email",99,12)

# TODO: call method 
print("====================================")
print(student1.intro())
print("====================================")