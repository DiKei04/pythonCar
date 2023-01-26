import os
import unittest
from .myCar import Car
from .log import Log


class TestCar(unittest.TestCase):
    f = Log()

    def setUp(self):
        self.c = Car(40, 20, 500, 30, 10)

    def test_stop(self):
        '''
        check if the car stopped
        '''
        try:
            x = self.c.stop()
            self.assertEqual(x, 0)
            self.f.print_in_txt(
                f' {str(os.getenv("stop_string"))} , result:{x} should receive 0'
                f'\n {self.test_stop.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_stop.__doc__)

    def test_start_True(self):
        '''
        check if the car start drive
        '''
        try:
            x = self.c.star()
            self.assertEqual(x, True)
            self.f.print_in_txt(
                f'{str(os.getenv("test_start"))}, result:{x} should receive True'
                f'\n {self.test_start_True.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_start_True.__doc__)

    def test_start_False(self):
        '''
        Checks if the vehicle can start when it is already in motion
        '''
        try:
            with self.assertRaises(TypeError):
                self.c.speed = int(os.getenv('speedA'))
                x = self.c.star()
                self.assertEqual(x, False)
            self.f.print_in_txt(
                f'{str(os.getenv("test_start_False"))},  check TypeError'
                f'\n {self.test_start_False.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_start_False.__doc__)

    def test_gearLevel_True(self):
        '''
        Checks if the gear is normal for speed
        '''
        try:
            self.c.speed = int(os.getenv('speedB'))
            x = self.c.gearLevel()
            self.assertEqual(x, 6)
            self.f.print_in_txt(
                f'{str(os.getenv("test_gearLevel_True"))}, result:{x} should receive 6'
                f'\n {self.test_gearLevel_True.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_gearLevel_True.__doc__)

    def test_gearLevel_False(self):
        '''
        Checks that the gear cannot be above level 6
        '''
        try:
            with self.assertRaises(OverflowError):
                self.c.speed = int(os.getenv('speedC'))
                self.c.gearLevel()
            self.f.print_in_txt(
                f'{str(os.getenv("test_gearLevel_False"))}, check OverFlowError'
                f'\n {self.test_gearLevel_False.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_gearLevel_False.__doc__)

    def test_checkFuel_True(self):
        '''
        Checks if there is enough fuel for the destination
        '''
        try:
            x = self.c.checkFuel(int(os.getenv('fuelA')))
            self.assertEqual(x, True)
            self.f.print_in_txt(
                f'{str(os.getenv("test_checkFuel_True"))}, result:{x} should receive True'
                f'\n {self.test_checkFuel_True.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_checkFuel_True.__doc__)

    def test_checkFuel_withRefueling_True(self):
        '''
        Checks if there is enough fuel for the destination provided there is money for fuel
        '''
        try:
            x = self.c.checkFuel(int(os.getenv('fuelB')))
            self.assertEqual(x, True)
            self.f.print_in_txt(
                f'{str(os.getenv("test_checkFuel_withRefueling_True"))}, result:{x} should receive True'
                f'\n {self.test_checkFuel_withRefueling_True.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_checkFuel_withRefueling_True.__doc__)

    def test_checkFuel_False(self):
        '''
        Checks that it is impossible to reach the destination without enough fuel
        '''
        try:
            with self.assertRaises(TypeError):
                x = self.c.checkFuel(int(os.getenv('fuelC')))
                self.assertEqual(x, False)
            self.f.print_in_txt(
                f'{str(os.getenv("test_checkFuel_False"))},  check TypeError'
                f'\n {self.test_checkFuel_False.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_checkFuel_False.__doc__)

    def test_checkMoney_true(self):
        '''
        Checks the amount of money corresponds to the amount of fuel that should be
        '''
        try:
            x = self.c.checkMoney()
            self.assertEqual(x, 90)
            self.f.print_in_txt(
                f'{str(os.getenv("test_checkMoney_true"))}, result:{x} should receive True'
                f'\n {self.test_checkMoney_true.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_checkMoney_true.__doc__)

    def test_checkMoney_False(self):
        '''
        Checks that you can't fill up fuel without money
        '''
        try:
            with self.assertRaises(TypeError):
                self.c.money = 0
                self.c.checkMoney()
            self.f.print_in_txt(
                f'{str(os.getenv("test_checkMoney_False"))}, check TypeError'
                f'\n {self.test_checkMoney_False.__doc__}')
        except Exception as e:
            self.f.print_error(e, self.test_checkMoney_False.__doc__)


if __name__ == '__main__':
    unittest.main()
