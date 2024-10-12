class Student:
    
    grade = 8
    print(f"Iam a Student af Grade {grade}")
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        


junaira = Student("Junaira", 12)
kashfia = Student("Kashfia", 15)
rifa = Student("Rifa", 14)


print(f"Name: {junaira.name}\nAge: {junaira.age}\n\n")
print(f"Name: {kashfia.name}\nAge: {kashfia.age}\n\n")
print(f"Name: {rifa.name}\nAge: {rifa.age}\n\n")

print(f"\n\nJunaira Grade: {junaira.grade}")
print(f"\n\kashfia Grade: {kashfia.grade}")
print(f"\n\rifa Grade: {rifa.grade}")