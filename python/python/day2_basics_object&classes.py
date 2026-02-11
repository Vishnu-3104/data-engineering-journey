#with function callback() and some methods added
class Car:
    max_speed = 120

    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = max(0, speed)

    def accelerate(self, acceleration):
        if acceleration < 0:
            raise ValueError("Acceleration cannot be negative. Use brake() instead.")
        
        new_speed = self.speed + acceleration
        self.speed = min(new_speed, self.max_speed)

    def brake(self, deceleration):
        if deceleration < 0:
            raise ValueError("Deceleration cannot be negative.")
        
        new_speed = self.speed - deceleration
        self.speed = max(new_speed, 0)

    def get_speed(self):
        return self.speed

    def __str__(self):
        return f"{self.color} {self.make} {self.model} traveling at {self.speed} km/h"


if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", "Blue")
    car2 = Car("Honda", "Civic", "Red", speed=50)
    car3 = Car("Audi", "A8", "Black")

    car1.accelerate(30)
    car2.brake(20)
    car3.accelerate(50)


    print(car1)
    print(car2)
    print(car3)

    # Testing limits
    car1.accelerate(200)   # Should cap at max_speed
    car2.brake(10)   # Should not go below 0
    car3.brake(10)
    car1.brake(20)

    print("\nAfter limit testing:")
    print(car1)
    print(car2)
    print(car3)
