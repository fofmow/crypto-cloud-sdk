from typing import Literal

from pydantic import BaseModel, constr, confloat


class InvoicePostback(BaseModel):
    """ Invoice postback
    https://docs.cryptocloud.plus/ru/api-reference-v2/postback
    """
    status: Literal["success"]
    invoice_id: constr(max_length=12)
    amount_crypto: confloat(ge=0)
    currency: constr(max_length=12)
    amount_usdt: confloat(ge=0)
    order_id: int | None = None
