from typing import Optional


class VehicleInfo:
    def __init__(self, vin: Optional[str], brand_model: str, license_plate: str, fuel_type: str, vehicle_type: str, color: Optional[str], doors: Optional[int], driver_id: Optional[int]):
        self.VIN = vin
        self.BrandModel = brand_model
        self.LicensePlate = license_plate
        self.FuelType = fuel_type
        self.VehicleType = vehicle_type
        self.Color = color
        self.Doors = doors
        self.DriverId = driver_id
