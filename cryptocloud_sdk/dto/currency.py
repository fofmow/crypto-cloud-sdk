from dataclasses import dataclass

from pydantic import BaseModel, conint

from .network import CurrencyNetwork


@dataclass(slots=True, frozen=True)
class SupportedCryptoCurrency:
    """ Supported Crypto Currencies
    https://docs.cryptocloud.plus/ru/api-reference-v2/create-invoice#opisanie-dopolnitelnykh-parametrov
    """
    USDT_TRC20 = "USDT_TRC20"
    USDC_TRC20 = "USDC_TRC20"
    TUSD_TRC20 = "TUSD_TRC20"
    USDT_ERC20 = "USDT_ERC20"
    USDC_ERC20 = "USDC_ERC20"
    TUSD_ERC20 = "TUSD_ERC20"
    USDD_TRC20 = "USDD_TRC20"
    SHIB_ERC20 = "SHIB_ERC20"
    USDT_BSC = "USDT_BSC"
    USDC_BSC = "USDC_BSC"
    TUSD_BSC = "TUSD_BSC"
    USDT_TON = "USDT_TON"
    BTC = "BTC"
    LTC = "LTC"
    ETH = "ETH"
    TRX = "TRX"
    BNB = "BNB"
    TON = "TON"


@dataclass(slots=True, frozen=True)
class SupportedFiatCurrency:
    USD = "USD"
    UZS = "UZS"
    KGS = "KGS"
    KZT = "KZT"
    AMD = "AMD"
    AZN = "AZN"
    BYN = "BYN"
    AUD = "AUD"
    TRY = "TRY"
    AED = "AED"
    CAD = "CAD"
    CNY = "CNY"
    HKD = "HKD"
    IDR = "IDR"
    INR = "INR"
    JPY = "JPY"
    PHP = "PHP"
    SGD = "SGD"
    THB = "THB"
    VND = "VND"
    MYR = "MYR"
    RUB = "RUB"
    UAH = "UAH"
    EUR = "EUR"
    GBP = "GBP"


class _BaseCurrency(BaseModel):
    id: conint(ge=0)
    code: str
    name: str
    is_email_required: bool
    stablecoin: bool
    icon_base: str
    icon_network: str
    icon_qr: str
    order: conint(ge=0)


class InvoiceCurrency(_BaseCurrency):
    network: CurrencyNetwork
    fullcode: str


class BalanceCurrency(_BaseCurrency):
    enable: bool | None = None
    obj_network: CurrencyNetwork
    short_code: str
