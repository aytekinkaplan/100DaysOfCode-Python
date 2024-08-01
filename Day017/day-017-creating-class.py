class User:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        return self.weight / (self.height * self.height)

    def description(self):
        if self.calculate_bmi() < 18.5:
            return "Underweight"
        elif self.calculate_bmi() < 25:
            return "Normal"
        elif self.calculate_bmi() < 30:
            return "Overweight"
        else:
            return "Obese"

    def __str__(self):
        return f"{self.name} is {self.description()}"


user1 = User("John", 25, 1.75, 75)
print(user1)
print(user1.calculate_bmi())

user2 = User("Jane", 30, 1.65, 60)
print(user2)
print(user2.calculate_bmi())
