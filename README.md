# Crypto Cloud SDK — простая асинхронная библиотека для работы с API [CryptoCloud](https://cryptocloud.plus/)

### 💡 Регистрация мерчанта и получение API ключей [описаны в документации](https://docs.cryptocloud.plus/ru/start/get-api-keys)

## Примеры использования / Use cases

```python
import asyncio
from datetime import date, timedelta

from cryptocloud_sdk import CryptoCloud, dto, errors


async def main():
    merchant = CryptoCloud(
        api_token="YOUR_API_TOKEN",
        shop_id="YOUR_SHOP_ID"
    )
    
    invoice: dto.CreatedInvoice = await merchant.create_invoice(
        invoice=dto.InvoiceInput(
            amount=250,
            currency="USD"  # or dto.currency.SupportedFiatCurrency.USD
        )
    )
    print(f"Invoice url is {invoice.link}")
    
    invoices: list[dto.InvoiceInfo] = await merchant.get_invoices(uuids=[invoice.uuid])
    
    canceled = await merchant.cancel_invoice(invoice.uuid)
    
    balances: list[dto.CoinBalance] = await merchant.get_balance()
    
    statictics: dto.Stats = await merchant.get_stats(
        start=date.today() - timedelta(days=3),
        end=date.today()
    )
    
    static_wallet: dto.StaticWallet = await merchant.create_static_wallet(
        currency="BTC",  # or dto.currency.SupportedCryptoCurrency.BTC , 
        identify="my-new-user-7"
    )
    
    # Handling errors
    try:
        await merchant.get_balance()
    except errors.UnauthorizedError:
        ...  # your code
    except errors.ForbiddenError:
        ...  # your code
    except errors.BadRequestError:
        ...  # your code


if __name__ == "__main__":
    asyncio.run(main())
```

####

## [Want to donate? Look at real app used CryptoCloud 😎](https://t.me/todonators_bot)

##


