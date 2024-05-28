class Transport:
    def move(self):
        pass


class WaterTransport(Transport):
    def swim(self):
        pass


class Ship(WaterTransport):
    pass


class Boat(WaterTransport):
    pass


class Submarine(WaterTransport):
    pass


class AirTransport(Transport):
    def fly(self):
        pass


class Plane(AirTransport):
    pass


class Airship(AirTransport):
    pass


class GroundTransport(Transport):
    def move(self):
        pass


class Trains(GroundTransport):
    pass


class Car(GroundTransport):
    pass


class Bicycle(GroundTransport):
    pass


class AnimalTransport(GroundTransport):
    pass


class SpaseTransport(Transport):
    pass


class SpaceShip(SpaseTransport):
    pass


class HypersonicTrain(SpaseTransport):
    pass
