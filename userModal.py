from pydantic import BaseModel
from typing import Optional

class Employees(BaseModel):
	email: str
	name: str
	mobile: str
	experienceYear: int

class Emp(BaseModel):
	email: str


