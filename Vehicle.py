from typing import Optional
from VehicleType import VehicleType
from FuelType import FuelType

class Vehicle:
    def __init__(self, vin_number: str, brand_model: str, license_plate: str, category: VehicleType, fuel: FuelType, color: Optional[str] = None, doors: Optional[int] = None, driver_id: Optional[int] = None):
        self._VinNumber = vin_number
        self._license_plate = license_plate
        self._brand_model = brand_model
        self.category = category
        self.fuel = fuel
        self.color = color
        self.doors = doors
        self.driver_id = driver_id

    @property
    def VinNumber(self) -> str:
        return self._VinNumber

    @VinNumber.setter
    def VinNumber(self, value: str):
        if value is None:
            raise Exception("Vehicle: set-VinNumber: NULL value")
        self._VinNumber = value

    @property
    def license_plate(self) -> str:
        return self._license_plate

    @license_plate.setter
    def license_plate(self, value: str):
        if value is None:
            raise Exception("Vehicle: set-LicensePlate: NULL value")
        self._license_plate = value

    @property
    def brand_model(self) -> str:
        return self._brand_model

    @brand_model.setter
    def brand_model(self, value: str):
        if value is None:
            raise Exception("Vehicle: set-BrandModel: NULL value")
        self._brand_model = value
