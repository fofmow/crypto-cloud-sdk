from datetime import date

from . import dto
from .http_executor import CryptoCloudHttpExecutor


class CryptoCloud:
    def __init__(
        self,
        api_token: str,
        shop_id: str,
        host="https://api.cryptocloud.plus",
        version: str = "/v2"
    ):
        self._http = CryptoCloudHttpExecutor(
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Token {api_token}"
            }
        )
        self._base_url = f"{host}{version}"
        self._shop_id = shop_id
    
    async def create_invoice(self, invoice: dto.InvoiceInput) -> dto.CreatedInvoice:
        """
        https://docs.cryptocloud.plus/ru/api-reference-v2/create-invoice#request-body
        """
        url = self._base_url + "/invoice/create"
        payload = invoice.model_dump(exclude_none=True) | {"shop_id": self._shop_id}
        
        _, body = await self._http.make_request(
            url=url,
            json=payload,
        )
        
        return dto.CreatedInvoice(**body.get("result"))
    
    async def get_invoices(self, uuids: list[str]) -> list[dto.InvoiceInfo]:
        """
        https://docs.cryptocloud.plus/ru/api-reference-v2/invoice-list#request-body
        """
        url = self._base_url + "/invoice/merchant/info"
        
        _, body = await self._http.make_request(
            url=url,
            json={"uuids": uuids},
        )
        
        return [dto.InvoiceInfo(**i) for i in body.get("result")]
    
    async def cancel_invoice(self, uuid: str) -> None:
        """ https://docs.cryptocloud.plus/ru/api-reference-v2/cancel-invoice#request-body
        
        Request will be executed successfully only when invoice has 'created' status
        :return None -> if canceled without any problem
        :return Exception -> when some param is not correct """
        
        url = self._base_url + "/invoice/merchant/canceled"
        
        _, body = await self._http.make_request(
            url=url,
            json={"uuid": uuid},
        )
    
    async def get_balance(
        self, in_currency: dto.SupportedCryptoCurrency | None = None
    ) -> list[dto.CoinBalance] | dto.CoinBalance:
        """
        https://docs.cryptocloud.plus/ru/api-reference-v2/balance#poluchit-balans
        """
        url = self._base_url + "/merchant/wallet/balance/all"
        
        _, body = await self._http.make_request(url=url)
        
        if in_currency:
            in_curr = [b for b in body.get("result") if b.get("currency").get("code") == in_currency]
            if in_curr:
                return dto.CoinBalance(**in_curr.pop())
        
        return [dto.CoinBalance(**i) for i in body.get("result")]
    
    async def get_stats(self, start: date, end: date) -> dto.Stats:
        """
        https://docs.cryptocloud.plus/ru/api-reference-v2/statistics#request-body
        """
        url = self._base_url + "/invoice/merchant/statistics"
        payload = {
            "start": start.strftime("%d.%m.%Y"),
            "end": end.strftime("%d.%m.%Y")
        }
        
        _, body = await self._http.make_request(
            url=url,
            json=payload,
        )
        
        return dto.Stats(**body.get("result"))
    
    async def create_static_wallet(self, currency: str, identify: str) -> dto.StaticWallet:
        """
        https://docs.cryptocloud.plus/ru/api-reference-v2/static-wallet#request-body
        """
        url = self._base_url + "/invoice/static/create"
        
        _, body = await self._http.make_request(
            url=url,
            json={
                "shop_id": self._shop_id,
                "currency": currency,
                "identify": identify,
            },
        )
        
        return dto.StaticWallet(**body.get("result"))
