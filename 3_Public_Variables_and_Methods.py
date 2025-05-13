class Car:
    def __init__(self,brand):
        self.brand = brand # public variable

    def start(self):
        print(f"{self.brand} Car Engine Started.\n")


if __name__ == "__main__":
    car1 = Car("\nHyundai")
    print(car1.brand)
    car1.start()        