class Car:
    def __init__(self, model: str, fuel_capacity: int):
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.fuel_level = 0  # изначально бак пустой
        self.odometer = 0
        self._fuel_consumption = 10  # 10 km per liter (можно изменить)

    def drive(self, distance: int):
        if distance < 0:
            raise Exception("Distance cannot be negative")
        required_fuel = distance / self._fuel_consumption
        if self.fuel_level < required_fuel:
            raise Exception("Не доедем жеж...")
        self.fuel_level -= required_fuel
        self.odometer += distance

    def refuel_car(self, amount: int):
        if amount <= 0:
            raise Exception("Refuel amount must be positive")
        if self.fuel_level + amount > self.fuel_capacity:
            raise Exception("Cannot refuel: exceeds fuel capacity")
        self.fuel_level += amount

    def get_current_fuel_level(self) -> int:
        return self.fuel_level
