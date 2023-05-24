from DomainFactory import DomainFactory
from FuelType import FuelType
from VehicleInfo import VehicleInfo
from VehicleType import VehicleType

class VehicleMapper:
    @staticmethod
    def map_dto_to_entity(vi):
        return DomainFactory.create_vehicle(vi.VIN, vi.BrandModel, vi.LicensePlate, VehicleType[vi.VehicleType], FuelType[vi.FuelType], vi.Color, vi.Doors, vi.DriverId)

    @staticmethod
    def map_entity_to_dto(v):
        return VehicleInfo(v.vin_number, v.brand_model, v.license_plate, v.fuel.name, v.category.name, v.color, v.doors, v.driver_id) if v is not None else None
