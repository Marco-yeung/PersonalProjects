'''
1. we would like to create a class, Swimmer, to store their name, age and time
2. To define a function to print their time 
3. create another class, Results, to store their results into a list and find the first one.
4. define a function to add swimmer to the lis
5. define a function to get the average swimmer among the list
'''

class Swimmer():
    def __init__(self, name, age, time):
        self.name = name
        self.age = age
        self.time = time

    def get_time(self):
        return self.time
    

class Results():
    def __init__(self, race, max_swimmers):
        self.race = race
        self.max_swimmers = max_swimmers
        self.swimmers = []
        

    def add_swimmer(self, swimmer):
        if len(self.swimmers) < self.max_swimmers:
            self.swimmers.append(swimmer)
            return True
        return False
    
    def get_average_time(self):
        value = 0
        for swimmer in self.swimmers:
            value += swimmer.get_time()
        return round(value/len(self.swimmers), 2)
    
p1 = Swimmer('Sam', 20, 1.05)
p2 = Swimmer('Tom', 20, 1.06)
p3 = Swimmer('Jerry', 20, 1.08)
p4 = Swimmer('Jerry', 20, 1.03)


result = Results("100M_Freestyle", 3)
result.add_swimmer(p1)
result.add_swimmer(p4)
result.add_swimmer(p2)
result.add_swimmer(p3)
print(result.get_average_time())