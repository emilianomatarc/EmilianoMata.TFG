
class Action:
    
    def __init__(self, order, name, param1, param2):
        self.order = order
        self.name = name
        self.param1 = param1
        self.param2 = param2

    def __str__(self):
        return f"{self.order} {self.name} {self.param1} {self.param2}"