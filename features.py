from pydantic import BaseModel


class Features(BaseModel):
    area: float
    perimeter: float
    compactness: float
    length: float
    width: float
    asymmetry: float
    kernel_length: float
