class Human:
    height = 180
    weight = 55

    def sleep(self, hours):
        print(self.weight * hours)

    def walk(self):
        print("walking")


# Human
hours = int(input("Enter the number of hours you sleep "))
man = Human()
man.sleep(hours)
man.walk()