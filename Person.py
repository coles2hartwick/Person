# Sam Cole
# 11/14/2019


class Person():

    def __init__(self, name, age, occupation, eye_color):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.eye_color = eye_color

    def description(self):
        return self.name + " is " + str(self.age) + " years old, they work as a " + self.occupation + " and their eye color is " + self.eye_color
