#  Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:



class dog:
    def __init__(self,name,age,coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color
    
    def description(self):
        return f"{self.name} is {self.age} year old"

    def get_info(self): 
        return f"{self.coat_color} is color of dog" 

class JackRussellTerrier(dog):
    def __init__(self, name, age,gender,birth_place,coat_color):
        super().__init__(name, age, coat_color)
        self.gender = gender
        self.birth_palce = birth_place

    def __str__(self):
        return f"\nJackRussellTerrier_name : {self.name}, \nJackRussellTerrier_age : {self.age},\nJackRussellTerrier_coat_color : {self.coat_color},\nJackRussellTerrier_gender : {self.gender},\nJackRussellTerrier_birth_place : {self.birth_palce}"

class Bulldog(dog):
    def __init__(self, name, age, coat_color,gender,health):
        super().__init__(name, age, coat_color)
        self.gender = gender
        self.health = health
    def __str__(self) -> str:
        return f"\nBulldog_name : {self.name},\nBulldog_age : {self.age},\nBulldog_coat_color : {self.coat_color},\nBulldog_gender : {self.gender},\nBulldog_health : {self.health}"


jackrusselterrior_name = input("Enter a jackrusselterrior_name :- ")
jackrusselterrior_age = int(input("Enter the age :- "))
jackrusselterrior_coat_color = input("Enter a coat_color :- ")
jackrusselterrior_gender = input("Enter gender :- ")
jackrusselterrior_birth_place = input("Enter birth_place:- ")
print("*"*40 )
Bulldog_name = input("Enter a Bulldog_name :- ")
Bulldog_age =  int(input("Enter the age :- "))
Bulldog_coat_color = input("Enter a coat_color :- ")
Bulldog_gender = input("Enter gender :- ")
Bulldog_health = input("Enter health :- ")
