class Person:
    def __init__(self,name):
        self.name = name


class Teacher(Person):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print(f"\nName: {self.name}.\nSubject: {self.subject}.\n")


teach = Teacher("Muneeb","Agentic AI")
teach.display()        