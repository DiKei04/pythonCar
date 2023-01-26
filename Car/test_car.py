import pytest
from .myCar import Car
import os
from Car.log import Log

f = Log()


@pytest.fixture
def c():
    return Car(40, 20, 500, 30, 10)


def test_stop(c):
    '''
    check if the car stopped
    :param c: the car
    '''
    try:
        x = c.stop()
        assert x == 0
        f.print_in_txt(f'The test "test_stop" passed successfully, result:{x} should receive 0'
                       f'\n {test_stop.__doc__}')
    except Exception as e:
        f.print_error(e, test_stop.__doc__)


def test_start_True(c):
    '''
    name: dima
    Date: 23/01/23
    check if the car start drive
    :param c: the car
    '''
    try:
        x = c.star()
        assert x == True
        f.print_in_txt(
            f'The test "test_start" passed successfully, result:{x} should receive True'
            f'\n {test_start_True.__doc__}')
    except Exception as e:
        f.print_error(e, test_start_True.__doc__)


def test_start_False(c):
    '''
    Checks if the vehicle can start when it is already in motion
    :param c: the car
    '''
    try:
        with pytest.raises(TypeError):
            c.speed = int(os.getenv('speedA'))
            x = c.star()
            assert x == False
        f.print_in_txt(f'The test "test_start" passed successfully,  check TypeError'
                       f'\n {test_start_False.__doc__}')
    except Exception as e:
        f.print_error(e, test_start_False.__doc__)


def test_gearLevel_True(c):
    '''
    Checks if the gear is normal for speed
    :param c: the car
    '''
    try:
        c.speed = int(os.getenv('speedB'))
        x = c.gearLevel()
        assert x == 6
        f.print_in_txt(
            f'The test "test_gearLevel" passed successfully, result:{x} should receive 6'
            f'\n {test_gearLevel_True.__doc__}')
    except Exception as e:
        f.print_error(e, test_gearLevel_True.__doc__)


def test_gearLevel_False(c):
    '''
    Checks that the gear cannot be above level 6
    :param c: the car
    '''
    try:
        with pytest.raises(OverflowError):
            c.speed = int(os.getenv('speedC'))
            c.gearLevel()
        f.print_in_txt(
            f'The test "test_gearLevelF" passed successfully, check OverFlowError'
            f'\n {test_gearLevel_False.__doc__}')
    except Exception as e:
        f.print_error(e, test_gearLevel_False.__doc__)


def test_checkFuel_True(c):
    '''
    Checks if there is enough fuel for the destination
    :param c: the car
    '''
    try:
        x = c.checkFuel(int(os.getenv('fuelA')))
        assert x == True
        f.print_in_txt(
            f'The test "test_checkFuelT" passed successfully, result:{x} should receive True'
            f'\n {test_checkFuel_True.__doc__}')
    except Exception as e:
        f.print_error(e, test_checkFuel_True.__doc__)


def test_checkFuel_withRefueling_True(c):
    '''
    Checks if there is enough fuel for the destination provided there is money for fuel
    :param c: the car
    '''
    try:
        x = c.checkFuel(int(os.getenv('fuelB')))
        assert x == True
        f.print_in_txt(
            f'The test "test_checkFuel_withRefueling" passed successfully, result:{x} should receive True'
            f'\n {test_checkFuel_withRefueling_True.__doc__}')
    except Exception as e:
        f.print_error(e, test_checkFuel_withRefueling_True.__doc__)


def test_checkFuel_False(c):
    '''
    Checks that it is impossible to reach the destination without enough fuel
    :param c: the car
    '''
    try:
        with pytest.raises(TypeError):
            x = c.checkFuel(int(os.getenv('fuelc')))
            assert x == False
        f.print_in_txt(
            f'The test "test_checkFuel" passed successfully,  check TypeError'
            f'\n {test_checkFuel_False.__doc__}')
    except Exception as e:
        f.print_error(e, test_checkFuel_False.__doc__)


def test_checkMoney_true(c):
    '''
    Checks the amount of money corresponds to the amount of fuel that should be
    :param c: the car
    '''
    try:
        x = c.checkMoney()
        assert x == 90
        f.print_in_txt(
            f'The test "test_checkMoney" passed successfully, result:{x} should receive True'
            f'\n {test_checkMoney_true.__doc__}')
    except Exception as e:
        f.print_error(e, test_checkMoney_true.__doc__)


def test_checkMoney_False(c):
    '''
    Checks that you can't fill up fuel without money
    :param c: the car
    '''
    try:
        with pytest.raises(TypeError):
            c.money = 0
            c.checkMoney()
        f.print_in_txt(
            f'The test "test_checkMoney" passed successfully, check TypeError'
            f'\n {test_checkMoney_False.__doc__}')
    except Exception as e:
        f.print_error(e, test_checkMoney_False.__doc__)
