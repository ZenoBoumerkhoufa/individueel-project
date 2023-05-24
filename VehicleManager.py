from VehicleMapper import VehicleMapper
class VehicleManager:
    def __init__(self, repo):
        self._repo = repo

    def get_all_vehicle_infos(self):
        vehicle_infos = []
        for vehicle in self._repo.get_all_vehicles():
            vehicle_infos.append(VehicleMapper.map_entity_to_dto(vehicle))
        return vehicle_infos
