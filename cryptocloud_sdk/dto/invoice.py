from datetime import datetime
from typing import Literal

from pydantic import BaseModel, confloat

from .currency import InvoiceCurrency
from .project import Project


class _BasePostInvoice(BaseModel):
    uuid: str
    expiry_date: datetime
    address: str
    side_commission: str
    amount: confloat(gt=0)
    amount_usd: confloat(gt=0)
    fee: confloat(gt=0)
    fee_usd: confloat(gt=0)
    service_fee: confloat(gt=0)
    service_fee_usd: confloat(gt=0)
    status: str
    currency: InvoiceCurrency
    project: Project
    test_mode: bool


class TimeToPay(BaseModel):
    minutes: int | None = 00
    hours: int | None = 2


class AddedInvoiceParamsInput(BaseModel):
    time_to_pay: TimeToPay | None = None
    email_to_send: str | None = None
    available_currencies: list[str] | None = None
    cryptocurrency: str | None = None
    period: Literal["month", "week", "day"] | None = None


class InvoiceInput(BaseModel):
    amount: confloat(gt=0)
    
    currency: str | None = "USD"
    order_id: str | None = None
    email: str | None = None
    
    add_fields: AddedInvoiceParamsInput | None = None


class CreatedInvoice(_BasePostInvoice):
    created: datetime
    amount_in_fiat: confloat(gt=0)
    fiat_currency: str
    side_commission_service: str
    is_email_required: bool
    link: str


class InvoiceInfo(_BasePostInvoice):
    received: confloat(ge=0)
    received_usd: confloat(ge=0)
    order_id: str | None = None
    side_commission_cc: str
