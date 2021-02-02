from PersonConstruct import Person


#   for better understanding of how personalities are built here is class with initialization defining arguments
# correlation
class Genie(Person):
    def __init__(self):
        super().__init__(
            hair="none", 
            eyes="foggy", 
            ears="none", 
            headshape="round", 
            height="small", 
            mouthSize="none", 
            language="high elfian", 
            skinColor="blue foggy"
        )
        
    def show_class(self):
        return "genie"
        
class Mandalorian(Person):
    def __init__(self):
        super().__init__("black", "small green", "small round", "round", "medium", "medium", "universal", "white")
        
    def show_class(self):
        return "mandalorian"
        
class Jedi(Person):
    def __init__(self):
        super().__init__("brown", "brown", "small round", "round", "tall", "small", "force", "brown")
        
    def show_class(self):
        return "jedi"
        
class Tatoiner(Person):
    def __init__(self):
        super().__init__("yellow", "blue", "small", "cubic", "medium", "small", "tatooinean", "black")
        
    def show_class(self):
        return "tatooiner"
        
class Loonie(Person):
    def __init__(self):
        super().__init__("white", "black", "small cubic", "cubic", "medium", "big", "lunar", "white")
        
    def show_class(self):
        return "loonie"
     
     
#   this is the most important class that collects all species in one base and can be accessed for requesting comparison operation
class PersonalitiesDB:
    def __init__(self):
        self.listOfPersonalities = [Genie(), Mandalorian(), Jedi(), Tatoiner(), Loonie()]