from pydantic import BaseModel, conint


class Project(BaseModel):
    id: conint(ge=0)
    name: str
    fail: str
    success: str
    logo: str | None = None
