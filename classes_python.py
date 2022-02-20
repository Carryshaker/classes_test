class Car:
    def __init__(self, model, color, engine):
        self.model = model
        self.color = color
        self.engine = engine
    def start(self):
        print(f"{self.model} car was started!")

class Big_Car(Car):
    def __init__(self, model, color, engine, load_capacity):
        super().__init__(model, color,engine)
        
        self.load_capacity=load_capacity
    
    def logistics(self):
        print(f"{self.model} on the way to Moscow! The driver took {self.load_capacity} tons!")
    
class Sportcar(Car):
    def __init__(self, model, color, engine, speed):
        super().__init__(model, color,engine)
        
        self.speed=speed
        
    def road(self):
        print(f"{self.model} on the way to formula-1! He's driving at {self.speed} M/H!")
    
class Bus(Car):
    def __init__(self, model, color, engine, workload):
        super().__init__(model, color,engine)
        
        self.workload=workload
        
    def work(self):
        print(f"{self.model} took passengers! The driver took {self.workload} people`s!")
    

b1=Big_Car("Scania", "Blue", 200, 150)
s1=Sportcar("Ferrari", "Red", 400, 250)
b2=Bus("LIAZ", "Brown", 100, 40)

b1.start()
b1.logistics()
s1.start()
s1.road()
b2.start()
b2.work()