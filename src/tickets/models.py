
from datetime import date
from enum import Enum
from pydantic import BaseModel


class ServiceType(str, Enum):
    repair = "repair"
    maintenance = "maintenance"
    installation = "installation"


class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Ticket(BaseModel):
    ticket_id: str
    customer_name: str
    service_type: ServiceType
    priority: Priority
    created_date: date
