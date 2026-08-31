from datetime import datetime
from pydantic import BaseModel, Field

class SecurityEvent(BaseModel):
    event_id: str = Field(min_length=3, max_length=100)
    timestamp: datetime
    source_ip: str
    event_type: str
    failed_logins: int = Field(default=0, ge=0)
    requests_per_minute: int = Field(default=0, ge=0)
    connections: int = Field(default=0, ge=0)
    bytes_transferred: int = Field(default=0, ge=0)
    hour: int = Field(default=12, ge=0, le=23)
