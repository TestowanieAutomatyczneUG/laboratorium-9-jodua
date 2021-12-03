from src.Car import Car


# Car system class
class CarImpl:
    def __init__(self, car: Car) -> None:
        self._car = car

    def car_fuel_check_message(self) -> str:
        if self._car.needsFuel():
            return "Low fuel"
        return "Fuel ok"

    def car_engine_temperature_message(self) -> str:
        engine_temperature = self._car.getEngineTemperature()
        if engine_temperature < 90:
            return "Temperature of engine is too low"
        elif engine_temperature > 104:
            return "Temperature of engine is too high"
        return "Temperature of engine is ok"

    def car_set_destination(self, destination) -> str:
        return f'GPS is set to ${self._car.driveTo(destination)}'
