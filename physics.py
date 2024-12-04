import math


def  area_of_circle():
     radius = float(input("Enter radius: "))
     area =2 *22/7 * radius
     print(area)

#area_of_circle()

def   calculate_velocity():
      distance = float(input('Enter your distance: '))
      time = int(input('Enter your time: '))
      velocity = distance/time
      print(velocity)

#calculate_velocity()

print('Welcome To Physics 101 Class')

print('Where we teach on the topic: Scalar/Vectors Quantity')
print('(a) Acceleration ')
print('(b) Speed ')
print('(c) Velocity ')
print('(d) Distance')
print('(e) Force ')

def a():
    velocity = float(input('Enter your velocity: '))
    time = int(input('Enter your time: '))
    a = velocity/time
    print(a)
a
def b():
    distance = float(input('Enter your distance: '))
    time = int(input('Enter your Time: '))
    b = distance/time
    print(b)

def c():
    displacement = float(input('Enter your displacement: '))
    time = int(input('Enter your time: '))
    c = displacement/time
    print(c)

def d():
    speed = float(input('Enter your speed: '))
    time = int(input('Enter your time: '))
    d = speed * time
    print(d)

def e():
    mass = float(input('Enter your mass: '))
    acceleration = int(input('Enter your acceleration: '))
    e = mass * acceleration
    print(e)

def main():
    choice = input('choose option')

    if choice == "a":
        a()

    if choice == "b":
        b()

    if choice == "c":
        c()

    if choice == "d":
        d()

    if choice == "e":
        e()


if __name__ == ' __main__':
        main()



