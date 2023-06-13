from fastapi import FastAPI, HTTPException
from starlette.responses import JSONResponse
from VehicleInfo import VehicleInfo
from VehicleManager import VehicleManager
from VehicleRepository import VehicleRepository
import re

VIN_PATTERN = r"^[A-HJ-NPR-Z0-9]{17}$"

app = FastAPI()
vehicle_manager = VehicleManager(VehicleRepository('mysql.affiche.me', 'stolos', 'db_allphifm_TEST', 'st0l0Sdb2324!'))


@app.get("/vehicles")
async def get_vehicles():
    try:
        vis = vehicle_manager.get_all_vehicle_infos()
        if not vis:
            raise HTTPException(status_code=404, detail="Not Found")
        return vis
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {ex}")


@app.get("/vehicles/{vin}", name="GetVehicleByVin")
async def get_vehicle_by_vin(vin: str):
    try:
        vi = vehicle_manager.get_vehicle_by_vin(vin)
        if vi is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return vi
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {ex}")


@app.post("/addVehicle", name="addVehicle", response_model=None)
async def add_vehicle(vi: VehicleInfo):
    try:
        if not re.match(VIN_PATTERN, vi.VIN):
            raise ValueError(f"{vi.VIN} is an invalid VIN number.")

        vehicle_manager.add_vehicle(vi)
        return JSONResponse(content={"message": "Vehicle added successfully"})
    except ValueError as ex:
        if "Duplicate entry" in str(ex) and "Vehicle.PRIMARY" in str(ex):
            raise HTTPException(status_code=400, detail=f"A vehicle with VIN {vi.VIN} already exists.")
        elif "Duplicate entry" in str(ex) and "Vehicle.uc_vehicle_licenseplate" in str(ex):
            raise HTTPException(status_code=400, detail=f"A vehicle with LP {vi.LicensePlate} already exists.")
        elif "Duplicate entry" in str(ex) and "Vehicle.uc_vehicle_driverid" in str(ex):
            raise HTTPException(status_code=400, detail=f"DriverID {vi.DriverId} already has a car.")
        else:
            raise HTTPException(status_code=400, detail=str(ex))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal server error")


@app.put("/updateVehicles", name="updateVehicles")
def update_vehicles(vi: VehicleInfo):
    try:
        vehicle_manager.update_vehicle(vi)
        return JSONResponse(content={"message": "Vehicle updated successfully"})
    except ValueError as ex:
        if "Duplicate entry" in str(ex) and "Vehicle.PRIMARY" in str(ex):
            raise HTTPException(status_code=400, detail=f"A vehicle with VIN {vi.VIN} already exists.")
        elif "Duplicate entry" in str(ex) and "Vehicle.uc_vehicle_licenseplate" in str(ex):
            raise HTTPException(status_code=400, detail=f"A vehicle with LP {vi.LicensePlate} already exists.")
        elif "VIN" in str(ex):
            raise HTTPException(status_code=400, detail=f"{vi.VIN} is an invalid VIN number.")
        elif "Duplicate entry" in str(ex) and "Vehicle.uc_vehicle_driverid" in str(ex):
            raise HTTPException(status_code=400, detail=f"DriverID {vi.DriverId} already has a car.")
    raise HTTPException(status_code=500)


@app.delete("/deleteVehicle", name="deleteVehicles")
def delete_vehicles(vin: str):
    try:
        if vehicle_manager.get_vehicle_by_vin(vin) is None:
            return HTTPException(status_code=404)
        vehicle_manager.delete_vehicle(vin)
        return JSONResponse(status_code=200, content={"message": "Vehicle deleted successfully"})
    except Exception as ex:
        return JSONResponse(status_code=500, content=f"Executed with exception: {ex}")


@app.get("/")
async def helloworld():
    return {"message": "HelloWorld"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
