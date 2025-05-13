class Employee:
    def __init__(self,name, salary,ssn):
        self.name = name # public attribute
        self._salary = salary # protected attribute
        self._ssn = ssn # private variable


if __name__ == "__main__":
    emp = Employee("Azfar", 60000, "895-987-097")

    print("Public Variable: ",emp.name) # directly accessible
    print("Protected Variable: ",emp._salary) # still accessible but not recommended

    try:
        emp.__ssn # Not directly accessible given an AttributeError
    except AttributeError:
        print("Cannot access private variable __ssn.")
    else:
         print("Private Variable: ",emp.__ssn)       