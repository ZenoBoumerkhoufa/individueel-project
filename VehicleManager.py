from typing import Optional

from Vehicle import Vehicle
from VehicleInfo import VehicleInfo
from VehicleRepository import VehicleRepository
from VehicleMapper import VehicleMapper


class VehicleManager:
    def __init__(self, repository: VehicleRepository):
        self.repository = repository

    def get_all_vehicle_infos(self):
        vehicle_infos = []
        for vehicle in self.repository.get_all_vehicles():
            vehicle_infos.append(VehicleMapper.map_entity_to_dto(vehicle))
        return vehicle_infos

    def get_vehicle_by_vin(self, vin: str) -> Optional[Vehicle]:
        return self.repository.get_vehicle_by_vin(vin)

    def add_vehicle(self, vehicle_info: VehicleInfo):
        self.repository.add_vehicle(VehicleMapper.map_dto_to_entity(vehicle_info))

    def update_vehicle(self, vehicle_info: VehicleInfo):
        self.repository.update_vehicle(VehicleMapper.map_dto_to_entity(vehicle_info))

    def delete_vehicle(self, vin: str):
        self.repository.delete_vehicle(vin)
