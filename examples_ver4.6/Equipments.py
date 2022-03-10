#Parent Class Controller 

class Abb(object):
    
    #__init__constructor for main information of the controller
    def __init__(self, name, model, diinput, dooutput, aiinput, aooutput, protocol):
        self.name = name
        self.model = model
        self.diinput = diinput
        self.dooutput = dooutput
        self.aiinput = aiinput
        self.aooutput = aooutput
        self.protocol = protocol
        
    def display(self):
        print(self.name)
        print(self.model)
        print(self.diinput)
        print(self.dooutput)
        print(self.aiinput)
        print(self.aooutput)
        print(self.protocol)
        
        
    def details(self):
        print("Controller brand is {}".format(self.name))
        print("Controller model is {}".format(self.model))
        print("Controller model is {}".format(self.diinput))
        print("Controller model is {}".format(self.dooutput))
        print("Controller model is {}".format(self.aiinput))
        print("Controller model is {}".format(self.aooutput))
        print("Controller model is {}".format(self.protocol))
        

#  child class Equipment
class Equipment(Abb):
    def __init__(self, name, model, diinput, dooutput, aiinput, aooutput, protocol, brand, horsepower):
        self.brand = brand 
        self.horsepower = horsepower
        
        
        # invoking the __init__ of the parent class
        Abb.__init__(self, name, model, diinput, dooutput, aiinput, aooutput, protocol)
        
    def details(self):
        print("Controller brand is {}".format(self.name))
        print('Controller model is {}'.format(self.model))
        print("Controller model is {}".format(self.diinput))
        print("Controller model is {}".format(self.dooutput))
        print("Controller model is {}".format(self.aiinput))
        print("Controller model is {}".format(self.aooutput))
        print("Controller model is {}".format(self.protocol))
        print('Equipment horsepower {}'.format(self.horsepower))
        

        
        
        
        
        
        
        