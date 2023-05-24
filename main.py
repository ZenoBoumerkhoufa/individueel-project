from fastapi import FastAPI
from fastapi import HTTPException

from VehicleManager import VehicleManager
from VehicleRepository import VehicleRepository

app = FastAPI()
_vehicleManager = VehicleManager(VehicleRepository('mysql.affiche.me', 'db_allphifm', 'stolos', 'st0l0Sdb2324!'))


@app.get("/vehicles")
async def get_vehicles():
    try:
        vis = _vehicleManager.get_all_vehicle_infos()
        if not vis:
            raise HTTPException(status_code=404, detail="Not Found")
        return vis
    except Exception as ex:
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
async def helloworld():
    return {"message": "HelloWorld"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
