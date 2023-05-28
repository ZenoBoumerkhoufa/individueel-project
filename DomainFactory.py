from FuelType import FuelType
from Vehicle import Vehicle
from VehicleType import VehicleType
from typing import Optional

class DomainFactory:
    @staticmethod
    def create_vehicle(vin: str, brand_model: str, plate: str, vehicle_type: VehicleType, fuel_type: FuelType, color: Optional[str] = None, doors: Optional[int] = None, driver_id: Optional[int] = None) -> Vehicle:
        try:
            return Vehicle(vin_number=vin, brand_model=brand_model, license_plate=plate, category=vehicle_type, fuel=fuel_type, color=color, doors=doors, driver_id=driver_id)
        except Exception as ex:
            raise Exception("DomainFactory - create_vehicle", ex)
