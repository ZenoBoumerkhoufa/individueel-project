from DomainFactory import DomainFactory
from FuelType import FuelType
from Vehicle import Vehicle
from VehicleInfo import VehicleInfo
from VehicleType import VehicleType

class VehicleMapper:
    @staticmethod
    @staticmethod
    def map_dto_to_entity(vi: VehicleInfo) -> Vehicle:
        try:
            vehicle_type = VehicleType(vi.VehicleType)
            fuel_type = FuelType(vi.FuelType)
            return DomainFactory.create_vehicle(
                vi.VIN, vi.BrandModel, vi.LicensePlate,
                vehicle_type, fuel_type,
                vi.Color, vi.Doors, vi.DriverId
            )
        except Exception as ex:
            raise Exception(f"Mapping to entity failed: {ex}")

    @staticmethod
    def map_entity_to_dto(v: Vehicle) -> VehicleInfo:
        try:
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
        except Exception as ex:
            raise Exception(f"Mapping to DTO failed: {ex}")
