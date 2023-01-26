import random
import os
from dotenv import load_dotenv


class Car:
    load_dotenv()

    def __init__(self, fuel, fuelConsumption, money, gearSpeed, fuelPrice):
        self.fuel = fuel
        self.fuelConsumption = fuelConsumption
        self.money = money
        self.gearSpeed = gearSpeed
        self.fuelPrice = fuelPrice
        self.speed = 0

    def drive(self, distance):
        '''
        the function start drive
        :param distance: the vehicle's travel distance
        :return: the car drive
        '''
        if self.star():
            if self.checkFuel(distance):
                self.speedF()
                self.gearLevel()
                self.stop()

    def stop(self):
        '''
        the function stop the car
        :return: the speed car
        '''
        self.speed = 0
        print('car stopped')
        return self.speed

    def star(self):
        '''
        the function check if the car start to travel
        :return:
        '''
        if self.speed == 0:
            print('Car start drive')
            return True
        # print("cant start speed not 0")
        raise TypeError('error, cant start speed not 0')
        return False

    def speedF(self):
        '''
        the function get the speed car drive
        :return: speed car
        '''
        self.speed = random.randint(int(os.getenv('min_speed')), int(os.getenv('max_speed')))
        return self.speed

    def gearLevel(self):
        '''
        the function receives speed and calculates which gear to drive
        :return: the level gear
        '''
        gearLevel = int((self.speed / self.gearSpeed)) + 1
        if gearLevel > int(os.getenv('max_gearLevel')):
            # print("error gear level cant be 6+")
            raise OverflowError('error, gear level cant be 6+')
        else:
            for i in range(gearLevel):
                print(f'level gear {i}')
        return gearLevel

    def checkFuel(self, distance):
        '''
        the function checking the amount of fuel to make sure you can cover the distance
        :param distance:
        :return: If there is enough fuel to go the desired distance
        '''
        if distance / self.fuelConsumption < self.fuel:
            return True
        if distance / self.fuelConsumption < self.checkMoney():
            return True
        raise TypeError('no fuel to drive this distance')
        return False

    def checkMoney(self):
        '''
        the function fills up with fuel for the amount of money there is
        :return: Returns amount of fuel after refueling
        '''
        if self.money > 0:
            self.fuel += self.money / self.fuelPrice
            return self.fuel
        raise TypeError('no money to refueling')
        return self.fuel
