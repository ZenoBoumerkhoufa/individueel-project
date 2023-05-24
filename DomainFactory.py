from FuelType import FuelType
from Vehicle import Vehicle
from VehicleType import VehicleType
from typing import Optional


class DomainFactory:
    @staticmethod
    def create_vehicle(vin: str, brand_model: str, plate: str, vehicle_type: VehicleType, fuel_type: FuelType, color: Optional[str] = None, doors: Optional[int] = None, driver_id: Optional[int] = None):
        try:
            return Vehicle(vin, brand_model, plate, vehicle_type, fuel_type, color, doors, driver_id)
        except Exception as ex:
            raise Exception("DomainFactory - NewVehicle", ex)
