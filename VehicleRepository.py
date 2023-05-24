from typing import List
import mysql.connector
from mysql.connector import Error
from Vehicle import Vehicle
from VehicleType import VehicleType
from FuelType import FuelType
from DomainFactory import DomainFactory


class VehicleRepository:
    def __init__(self, host: str, database: str, user: str, password: str):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def get_all_vehicles(self) -> List[Vehicle]:
        vehicles = []
        try:
            connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            cursor = connection.cursor(dictionary=True)
            cursor.execute('SELECT * FROM Vehicle v LEFT JOIN Driver d ON v.DriverID=d.DriverID WHERE v.Deleted=0;')
            rows = cursor.fetchall()

            for row in rows:
                vinDB = row['VIN']
                brandModel = row['BrandModel']
                plate = row['LicensePlate']
                fuel_type = FuelType[row['FuelType']]
                vehicle_type = VehicleType[row['VehicleType']]
                color = row['Color'] if row['Color'] else None
                doors = row['Doors'] if row['Doors'] else None
                driver_id = row['DriverID'] if row['DriverID'] else None

                vehicle = DomainFactory.create_vehicle(vinDB, brandModel, plate, vehicle_type, fuel_type, color, doors, driver_id)

                vehicles.append(vehicle)

            cursor.close()
        except Error as e:
            print(f"Error connecting to MySQL database: {e}")
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
        return vehicles
