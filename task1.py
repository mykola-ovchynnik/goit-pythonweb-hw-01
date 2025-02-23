import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(
    logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
)
logger.addHandler(handler)


class Vehicle(ABC):
    def __init__(self, make: str, model: str) -> None:
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} -> engine started")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} -> engine started")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        logger.info(f"Creating a US spec car")
        return Car(f"{make} (US Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        logger.info(f"Creating a US spec motorcycle")
        return Motorcycle(f"{make} (US Spec)", model)


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        logger.info(f"Creating a EU spec car")
        return Car(f"{make} (EU Spec)", model)

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        logger.info(f"Creating a EU spec motorcycle")
        return Motorcycle(f"{make} (EU Spec)", model)


def main():
    us_factory = USVehicleFactory()
    us_factory.create_car("Ford", "Mustang").start_engine()
    us_factory.create_motorcycle("Harley-Davidson", "Sportster").start_engine()

    eu_factory = EUVehicleFactory()
    eu_factory.create_car("Toyota", "Corolla").start_engine()
    eu_factory.create_motorcycle("Yamaha", "MT-07").start_engine()


# Використання
if __name__ == "__main__":
    main()
