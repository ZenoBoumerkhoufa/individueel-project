from DomainFactory import DomainFactory
from FuelType import FuelType
from Vehicle import Vehicle
from VehicleInfo import VehicleInfo
from VehicleType import VehicleType

class VehicleMapper:
    @staticmethod
    def map_dto_to_entity(vi: VehicleInfo) -> Vehicle:
        return DomainFactory.create_vehicle(
            vi.VIN, vi.BrandModel, vi.LicensePlate,
            VehicleType[vi.VehicleType], FuelType[vi.FuelType],
            vi.Color, vi.Doors, vi.DriverId
        )

    @staticmethod
    def map_entity_to_dto(v: Vehicle) -> VehicleInfo:
        return VehicleInfo(
            VIN=v.VinNumber,
            BrandModel=v.brand_model,
            LicensePlate=v.license_plate,
            FuelType=v.fuel.value,
            VehicleType=v.category.value,
            Color=v.color,
            Doors=v.doors,
            DriverId=v.driver_id
        )
