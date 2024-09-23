class animal:
    def breate(self):
        print("Breathing")

class fish(animal):  #Inheritence
    def breate(self):
        super().breate()   #super class concept
        print("Under water")
goat=animal()
goat.breate()
whale=fish()
whale.breate()