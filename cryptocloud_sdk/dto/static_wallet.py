from pydantic import BaseModel

from .currency import BalanceCurrency


class StaticWallet(BaseModel):
    uuid: str
    address: str
    currency: BalanceCurrency
