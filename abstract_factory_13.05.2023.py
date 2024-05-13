from __future__ import annotations
from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def drive(self):
        pass

class CarFactory(ABC):
    def produce_car(self) -> Car:
        pass

class ElectricCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return ElectricCar()

class PetrolCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return PetrolCar()

class HybridCarFactory(CarFactory):
    def produce_car(self) -> Car:
        return HybridCar()

class ElectricCar(Car):
    def drive(self):
        print("Driving an electric car.")

class PetrolCar(Car):
    def drive(self):
        print("Driving a petrol car.")

class HybridCar(Car):
    def drive(self):
        print("Driving a hybrid car.")
