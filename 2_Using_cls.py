class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        print(f"\nTotal objects created: {cls.count}.\n")


if __name__ == "__main__":
    obj1 = Counter()
    obj2 = Counter()
    obj3 = Counter()
    obj4 = Counter()
    obj5 = Counter()
    obj6 = Counter()
    obj7 = Counter()
    obj8 = Counter()
    obj9 = Counter()
    obj10 = Counter()

    Counter.display_count()

    