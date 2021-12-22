from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    @abstractmethod
    def car(self) -> None:
        pass

    @abstractmethod
    def wheels(self) -> None:
        pass

    @abstractmethod
    def engine(self) -> None:
        pass

    @abstractmethod
    def turbo(self) -> None:
        pass

    @abstractmethod
    def body(self) -> None:
        pass


class CarBuilder(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Car()

    @property
    def car(self) -> Car:
        product = self._product
        self.reset()
        return product

    def wheels(self) -> None:
        self._product.add("Колеса")

    def engine(self) -> None:
        self._product.add("Двигатель")

    def body(self) -> None:
        self._product.add("Кузов")
    def turbo(self) -> None:
        self._product.add("Турбина")    
class Car():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Части автомобиля: {', '.join(self.parts)}", end="")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder
    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def TurboCar(self) -> None:
        self.builder.wheels()
        self.builder.engine()
        self.builder.body()
        self.builder.turbo()

    def AtmoCar(self) -> None:
        self.builder.wheels()
        self.builder.engine()
        self.builder.body()    

if __name__ == "__main__":
    director = Director()
    builder = CarBuilder()
    director.builder = builder

    print("Турбовый автомобиль: ")
    director.TurboCar()
    builder.car.list_parts()
    print("\n")
    print("Автомобиль без турбины: ")
    director.AtmoCar()
    builder.car.list_parts()

