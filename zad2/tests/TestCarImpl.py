from src.CarImpl import CarImpl
from src.Car import Car
from unittest.mock import Mock
from unittest import TestCase
from assertpy import assert_that


class TestCarImpl(TestCase):
    def test_car_fuel_check_fuel_ok(self) -> None:
        car = Car()
        car.needsFuel = Mock(name="needsFuel")
        car.needsFuel.return_value = False
        car_impl = CarImpl(car)
        assert_that(car_impl.car_fuel_check_message()).is_equal_to("Fuel ok")

    def test_car_fuel_check_fuel_low(self) -> None:
        car = Car()
        car.needsFuel = Mock(name="needsFuel")
        car.needsFuel.return_value = True
        car_impl = CarImpl(car)
        assert_that(car_impl.car_fuel_check_message()).is_equal_to("Low fuel")

    def test_car_engine_temperature_message_too_low(self) -> None:
        car = Car()
        car.getEngineTemperature = Mock(name="getEngineTemperature")
        car.getEngineTemperature.return_value = 50
        car_impl = CarImpl(car)
        assert_that(car_impl.car_engine_temperature_message()
                    ).ends_with("too low")

    def test_car_engine_temperature_message_too_high(self) -> None:
        car = Car()
        car.getEngineTemperature = Mock(name="getEngineTemperature")
        car.getEngineTemperature.return_value = 150
        car_impl = CarImpl(car)
        assert_that(car_impl.car_engine_temperature_message()
                    ).ends_with("too high")

    def test_car_engine_temperature_message_ok(self) -> None:
        car = Car()
        car.getEngineTemperature = Mock(name="getEngineTemperature")
        car.getEngineTemperature.return_value = 100
        car_impl = CarImpl(car)
        assert_that(car_impl.car_engine_temperature_message()
                    ).ends_with("is ok")

    def test_car_set_destination(self) -> None:
        car = Car()
        trip_destination = "Terespol"
        car.driveTo = Mock(name="driveTo")
        car.driveTo.return_value = trip_destination
        car_impl = CarImpl(car)
        assert_that(car_impl.car_set_destination(trip_destination)
                    ).is_equal_to(f'GPS is set to ${trip_destination}')
