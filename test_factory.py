import pytest

from factory import make, no_make, InstantiationError, factory


class Car:

    @no_make
    def __init__(self, key: any, color: str):
        self.color = color
        print(f"Created with color: {color} and key: {key}")

    @classmethod
    @make
    def make_red_car(cls, key):
        """Creates a red car"""
        return Car(key, "red")

    @classmethod
    @make
    def make_blue_car(cls, key):
        """Creates a blue car"""
        return Car(key, "blue")


@factory
class Cycle:

    def __init__(self, key: any, color: str):
        self.color = color
        print(f"Created Cycle with color: {color} and key: {key}")

    @classmethod
    @make
    def make_green_cycle(cls, key):
        """Creates a green cycle"""
        return Cycle(key, "green")

    @classmethod
    @make
    def make_yellow_cycle(cls, key):
        """Creates a yellow cycle"""
        return Cycle(key, "yellow")


def test_instantiate_car_using_factory_method():
    car = Car.make_red_car()
    assert car.color == "red"
    car = Car.make_blue_car()
    assert car.color == "blue"


def test_correct_function_wrapping_for_cars():
    assert Car.make_red_car.__name__ == "make_red_car"
    assert Car.make_red_car.__doc__ == "Creates a red car"
    assert Car.make_blue_car.__name__ == "make_blue_car"
    assert Car.make_blue_car.__doc__ == "Creates a blue car"


def test_instantiate_car_without_factory_method_fails():
    with pytest.raises(InstantiationError):
        Car(0, "green")
    with pytest.raises(InstantiationError):
        Car(None, "green")
    with pytest.raises(InstantiationError):
        Car(object(), "green")


def test_instantiate_cycle_using_factory_method():
    cycle = Cycle.make_green_cycle()
    assert cycle.color == "green"
    cycle = Cycle.make_yellow_cycle()
    assert cycle.color == "yellow"


def test_correct_function_wrapping_for_cycles():
    assert Cycle.make_green_cycle.__name__ == "make_green_cycle"
    assert Cycle.make_green_cycle.__doc__ == "Creates a green cycle"
    assert Cycle.make_yellow_cycle.__name__ == "make_yellow_cycle"
    assert Cycle.make_yellow_cycle.__doc__ == "Creates a yellow cycle"


def test_instantiate_cycle_without_factory_method_fails():
    with pytest.raises(InstantiationError):
        Cycle(0, "purple")
    with pytest.raises(InstantiationError):
        Cycle(None, "purple")
    with pytest.raises(InstantiationError):
        Cycle(object(), "purple")
