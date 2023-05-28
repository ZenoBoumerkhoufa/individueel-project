from typing import Optional
from pydantic import BaseModel, Field

class VehicleInfo(BaseModel):
    VIN: str
    BrandModel: str = Field(..., title="Brand Model")
    LicensePlate: str = Field(..., title="License Plate")
    FuelType: str = Field(..., title="Fuel Type")
    VehicleType: str = Field(..., title="Vehicle Type")
    Color: Optional[str]
    Doors: Optional[int]
    DriverId: Optional[int]

