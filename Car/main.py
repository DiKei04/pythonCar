from myCar import Car
from log import Log

if __name__ == '__main__':
    f = Log()
    c = Car(40, 20, 500, 30, 10)

    print(c.drive(800))


