class Dog:
    
    num_of_dogs = 0
    def __init__(self, name = "unknown"):
        self.name = name
        
        Dog.num_of_dogs += 1
        
    @staticmethod
    def getNumOfDog():
        print("there are currently {} dogs".format(Dog.num_of_dogs))
        

def main():
    spots = Dog("spots")
    doug = Dog("doug") 