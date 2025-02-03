from pydantic import BaseModel, conint, confloat


class StatsCount(BaseModel):
    all: conint(ge=0)
    created: conint(ge=0)
    paid: conint(ge=0)
    overpaid: conint(ge=0)
    partial: conint(ge=0)
    canceled: conint(ge=0)


class StatsAmount(BaseModel):
    all: confloat(ge=0)
    created: confloat(ge=0)
    paid: confloat(ge=0)
    overpaid: confloat(ge=0)
    partial: confloat(ge=0)
    canceled: confloat(ge=0)


class Stats(BaseModel):
    count: StatsCount
    amount: StatsAmount
