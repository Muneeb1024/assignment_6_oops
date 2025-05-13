class Student:

    def __init__(self,name:str,marks:int):
        self.name = name
        self.marks = marks

    def display(self):
        """Display Student Details"""
        print(f"\nStudent Name : {self.name}.\nMarks : {self.marks}.\n")

if __name__ ==  "__main__":
    s1 = Student("Muneeb", 98)
    s1.display()        
