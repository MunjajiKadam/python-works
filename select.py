class test :
    def __init__(self ,username, password):
        self.username = username
        self.password = password
        print("this is a  class test class 1 constructor ")
     
    def intro1(self):
        print(self.username)
        
        print("this is a  class test class 1 method 1")    
        

class intro(test):
    def __init__(self, username, password):
        super().__init__(username, password)
        
        print("this is a  class intro class 2 constructor")
     
    def intro3(self):
        print("this is a  class intro    class 2 method 3")    


obj1 = intro("munjaji", "1234") 
obj1.intro1()
obj1.intro3()
