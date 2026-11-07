#1
activity1_answers="""

1
.a. What is duck typing, as explained in the video?
Duck typing means Python doesn't care about an object's actual class or what family it comes from.
As long as it has the right method, Python can work with it. It follows the saying "if it walks like 
a duck and quacks like a duck, it's a duck"—meaning if an object has  the method you're trying to
call, Python will just run it without needing them to share a parent class.

b. What did the Car class need to have so it could work inside the 
same loop as Dog and Cat, even if it does not inherit from the Animal
class?
The Car class just needed to have the exact same method name (like make_sound()) that the loop was 
looking for, even though it's a vehicle and completely unrelated to the animals.
"""


#2
class Car:
    def move(self):
        print("The car drives on the road.")


class Boat:
    def move(self):
        print("The boat sails on water.")


class Drone:
    def move(self):
        print("The drone flies in the sky.")


def start_trip(vehicle):
    vehicle.move()


if __name__ == "__main__":
    my_car = Car()
    my_boat = Boat()
    my_drone = Drone()

    start_trip(my_car)
    start_trip(my_boat)
    start_trip(my_drone)
#3
activity1_answers = """
How does the code in 2.2 demonstrate polymorphism? 
The code shows polymorphism because Car, Boat, and Drone are completely different classes that 
don't share a parent class, but they all use the exact same method name (move()). When the function 
runs, it calls .move() for each one, and Python automatically figures out which object it is and 
does the right action. It proves that one single command can do different things depending on the 
object, which is what polymorphism is all about same name, different behavior. """