class Vehicle:
    
    
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage 
        
        
tesla = Vehicle(180, 0)
lambo = Vehicle(350, 6)


print("Tesla Max Speed: ", tesla.max_speed)
print("Tesla Mileage: ", tesla.mileage)

print()

print("Lamborgini Max Speed: ", lambo.max_speed)
print("Lamborgini Mileage: ", lambo.mileage)