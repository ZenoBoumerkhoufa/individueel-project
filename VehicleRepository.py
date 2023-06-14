from typing import List, Optional
import mysql.connector
from Vehicle import Vehicle
from VehicleType import VehicleType
from FuelType import FuelType
from DomainFactory import DomainFactory


class VehicleRepository:
    def __init__(self, host: str, user: str, database: str, password: str):
        self.host = host
        self.user = user
        self.database = database
        self.password = password
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def get_all_vehicles(self) -> List[Vehicle]:
        global cursor
        vehicles = []
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
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

        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

        finally:
            if cursor:
                cursor.close()
            self.disconnect()

        return vehicles

    def get_vehicle_by_vin(self, vin: str) -> Optional[Vehicle]:
        v = None
        cursor = None

        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT * FROM Vehicle v LEFT JOIN Driver d ON v.DriverID=d.DriverID WHERE VIN = %s AND v.Deleted=0;",
                (vin,))
            row = cursor.fetchone()

            if row:
                vinDB = row['VIN']
                brandModel = row['BrandModel']
                plate = row['LicensePlate']
                fuel_type = FuelType[row['FuelType']]
                vehicle_type = VehicleType[row['VehicleType']]
                color = row['Color'] if row['Color'] else None
                doors = row['Doors'] if row['Doors'] else None
                driver_id = row['DriverID'] if row['DriverID'] else None

                v = DomainFactory.create_vehicle(vinDB, brandModel, plate, vehicle_type, fuel_type, color, doors, driver_id)

        except mysql.connector.Error as ex:
            raise ValueError(f"Failed to retrieve vehicle: {ex}")

        finally:
            if cursor:
                cursor.close()
            self.disconnect()

        return v

    def add_vehicle(self, vehicle):
        print(f"{vehicle}")
        cursor = None
        try:
            self.connect()
            sql = "INSERT INTO Vehicle (VIN, BrandModel, LicensePlate, VehicleType, FuelType, Color, Doors, DriverID, Deleted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor = self.connection.cursor()
            cursor.execute(sql, (
                vehicle._VinNumber,
                vehicle._brand_model,
                vehicle._license_plate,
                vehicle.category.value,
                vehicle.fuel.value,
                vehicle.color,
                vehicle.doors,
                vehicle.driver_id,
                0,
            ))
            self.connection.commit()

        except mysql.connector.Error as ex:
            raise ValueError(f"Failed to add vehicle: {ex}")

        finally:
            if cursor:
                cursor.close()
            self.disconnect()

    def update_vehicle(self, vehicle):
        cursor = None
        try:
            self.connect()
            sql = "UPDATE Vehicle SET BrandModel=%s, LicensePlate=%s, VehicleType=%s, FuelType=%s, Color=%s, Doors=%s, DriverID=%s WHERE VIN=%s;"
            cursor = self.connection.cursor()
            cursor.execute(sql, (
                vehicle._brand_model,
                vehicle._license_plate,
                vehicle.category.value,
                vehicle.fuel.value,
                vehicle.color,
                vehicle.doors,
                vehicle.driver_id,
                vehicle._VinNumber
            ))
            self.connection.commit()

        except mysql.connector.Error as ex:
            raise ValueError(f"Failed to update vehicle: {ex}")

        finally:
            if cursor:
                cursor.close()
            self.disconnect()

    def delete_vehicle(self, vin: str):
        cursor = None
        try:
            self.connect()
            sql = "UPDATE Vehicle SET Deleted = %s WHERE VIN = %s;"
            cursor = self.connection.cursor()
            cursor.execute(sql, (
                1,
                vin
            ))
            self.connection.commit()
        except mysql.connector.Error as ex:
            raise ValueError(f"Failed to delete vehicle: {ex}")

        finally:
            if cursor:
                cursor.close()
            self.disconnect()
