from pydantic import BaseModel, confloat

from .currency import BalanceCurrency


class CoinBalance(BaseModel):
    currency: BalanceCurrency
    balance_crypto: confloat(ge=0)
    balance_usd: confloat(ge=0)
    available_balance: confloat(ge=0)
    available_balance_usd: confloat(ge=0)
