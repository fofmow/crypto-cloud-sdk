from pydantic import BaseModel, conint


class CurrencyNetwork(BaseModel):
    code: str
    id: conint(ge=0)
    icon: str
    fullname: str
