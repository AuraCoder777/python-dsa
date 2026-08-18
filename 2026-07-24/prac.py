                                                                          #Creating Class     
class car:
    
    def __init__(self,brand,color):                                       #initializes the object’s attributes
                                                                          #Attributes(means variables)
        self.brand=brand                                                      
        self.color=color
        
    def display(self):                                                    #Function to display attributes
        print(f"Brand : {self.brand}\nColor : {self.color}")
        
c1=car("BWM","Red")
c1.display()