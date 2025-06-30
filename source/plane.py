class Plane:
    def __init__(self, id: int, speed: int, motors: int = 1) -> None:
        self.id = id
        self.speed = speed
        self.motors = motors

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Plane):
            return False
        return (
            self.id == other.id and \
            self.speed == other.speed and \
            self.motors == other.motors
        )

    def add_motor(self, additional_speed: int) -> None:
        self.speed += additional_speed
        self.motors += 1

    def get_id(self) -> int:
        return self.id

    def get_speed(self) -> int:
        return self.speed

    def get_motors(self) -> int:
        return self.motors
